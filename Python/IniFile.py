'''
IniFile class
Haikun Huang
[section]
key=valus;comment
'''

class IniFile:
	'''
	IniFile read
	'''
	# draw ata dictionary
	# {section:{key:[value,comment]}}
	data = {}
	__curSection=''
	
  # load a inifile 
	def Load(self, filepath):
		with open(filepath, 'r') as f:
			for line in f:
				line = line.strip('\n').strip()
				# empty line
				if (len(line) == 0):
					...
					
				# comment
				elif (line.startswith(';')):
					...
					
				# section
				elif (line.startswith('[')):
					section = line
					comment = ''
					if (';' in section):
						section, comment = section.split(';', 1)
						
					section = section.strip().lstrip('[').rstrip(']')
					# strip the string
					section = section.strip()
					comment = comment.strip()
					# print('section = ' + section)
					# print('comment = ' + comment)
					
					# if not contain the section, create a new section
					self.curSection = section
					if (self.curSection not in self.data):
						self.data[self.curSection] = {}
					
					
				# key=value;omment
				else:
					key, value = line.split('=', 1)
					comment = ''
					if (';' in value):
					  value,comment = value.split(';', 1)
					# strip the strings
					key = key.strip()
					value = value.strip()
					comment = comment.strip()
					# print('  key = ' + key)
					# print('  value = ' + value)
					# print('  comment = ' + comment)
					
					self.data[self.curSection][key]=[value, comment]
				 
	# has section
	def HasSection(self, section):
		return (section in self.data)
				 
				 
				 
    # get string
	def GetString(self, section,key,defaultValue=''):
		if (section in self.data):
			if(key in self.data[section]):
				return self.data[section][key][0]
		return defaultValue

	# get int
	def GetInt(self, section,key,defaultValue=0):
		return int(self.GetString(section, key, defaultValue))
	
	
# main
if(__name__ =='__main__'):
	# print('Inifile class.')
	inif = IniFile()
	inif.Load('file.txt')
	print(inif.data)
	k = inif.GetString('section','key', 0)
	print(k)
	print(inif.GetInt('section', 'int',0))
	print(str(inif.HasSection('section')))
	



		
