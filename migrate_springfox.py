import re
import glob

for filepath in glob.iglob('./**/*.java', recursive=True):
	with open(filepath, encoding='utf8') as file:
		s = file.read()    
	print("current file : ", file)    
	# remvove @EnableSwagger2
	s = re.sub('import springfox.documentation.swagger2.annotations.EnableSwagger2;', '', s);
	s = re.sub('@EnableSwagger2', '', s);
	# remove BeanValidatorPluginsConfiguration
	s = re.sub('import springfox.bean.validators.configuration.BeanValidatorPluginsConfiguration;', '', s);
	s = re.sub('@Import\(BeanValidatorPluginsConfiguration.class\)', '', s);
	# Docket -> GroupedOpenApi
	s = re.sub('import springfox.documentation.spring.web.plugins.Docket;', 'import org.springdoc.core.GroupedOpenApi;', s);
	s = re.sub('public Docket', 'public GroupedOpenApi', s); 
	# io.swagger imports -> io.swagger.v3.oas imports
	s = re.sub('import io.swagger.annotations.Api;', 'import io.swagger.v3.oas.annotations.tags.Tag;', s)
	s = re.sub('import io.swagger.annotations.ApiImplicitParam;', 'import io.swagger.v3.oas.annotations.Parameter;', s)
	s = re.sub('import io.swagger.annotations.ApiImplicitParams;', 'import io.swagger.v3.oas.annotations.Parameters;', s)
	s = re.sub('import io.swagger.annotations.ApiModel;', 'import io.swagger.v3.oas.annotations.media.Schema;', s)
	s = re.sub('import io.swagger.annotations.ApiModelProperty;', 'import io.swagger.v3.oas.annotations.media.Schema;', s)
	s = re.sub('import io.swagger.annotations.ApiOperation;', 'import io.swagger.v3.oas.annotations.Operation;', s)
	s = re.sub('import io.swagger.annotations.ApiParam;', 'import io.swagger.v3.oas.annotations.Parameter;', s)
	s = re.sub('import io.swagger.annotations.ApiResponse;', 'import io.swagger.v3.oas.annotations.responses.ApiResponse;', s)
	s = re.sub('import io.swagger.annotations.ApiResponses;', 'import io.swagger.v3.oas.annotations.responses.ApiResponses;', s)
	# Api -> Tag
	s = re.sub(r'\@RequestMapping\((.*?)\)\n\@Api\(\"(.*?)\"\)', r'@RequestMapping(\1)\n@Tag(name = \1, description = "\2")', s, flags = re.M)
	s = re.sub('@Api\(\"', '@Tag(description = "', s)
	# ApiModelProperty -> Schema
	s = re.sub('@ApiModelProperty\(value', '@Schema(description', s)
	s = re.sub('@ApiModelProperty\(notes', '@Schema(description', s)
	s = re.sub('@ApiModelProperty\("', '@Schema(description = "', s)
	# ApiOperation -> Operation
	s = re.sub('@ApiOperation\(value =', '@Operation(summary =', s)
	s = re.sub('@ApiOperation\(', '@Operation(summary =', s)
	# ApiParam -> Parameter
	s = re.sub(r'\@ApiParam\(name \= (.*?)\, value \= (.*?)\)', r'@Parameter(name = \1, description = \2)', s)
	s = re.sub('@ApiParam', '@Parameter', s)
	# ApiResponse -> ApiResponse
	s = re.sub(r'\@ApiResponses\(\{\@ApiResponse\(code \= (.*?)\, message \= \"(.*?)\"\)\}\)', r'@ApiResponse(responseCode = "\1", description = "\2")', s, flags = re.M);
	s = re.sub(r'@ApiResponse\(code \= (.*?)\, message \= \"(.*?)\"\)', r'@ApiResponse(responseCode = "\1", description = "\2")', s);
	with open(filepath, "w", encoding='utf8') as file:
		file.write(s)