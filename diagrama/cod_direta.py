linhaGlobal = 0
colunaGlobal = 0
def cod_direta():
	state = 'A'
	c = ''
	id = ''
	global linhaGlobal
	global colunaGlobal
	coluna = colunaGlobal
	lerProx = True
	while True:
		match state:
			case 'A':
				if c not in ['\n', '\t', ' ']:
					id = c 
				else:
					id = ''
				if lerProx:
					c = nextChar()
					id += c
					colunaGlobal += 1
				else:
					lerProx = True
				if c.lower() == 'a':
					state = 'B'
					print('leu caracter a foi para B')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'D'
					print('leu caracter c foi para D')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'E'
					print('leu caracter e foi para E')
				elif c.lower() == 'f':
					state = 'F'
					print('leu caracter f foi para F')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'G'
					print('leu caracter i foi para G')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'H'
					print('leu caracter p foi para H')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'I'
					print('leu caracter r foi para I')
				elif c.lower() == 's':
					state = 'J'
					print('leu caracter s foi para J')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'K'
					print('leu caracter < foi para K')
				elif c.lower() == '-':
					state = 'L'
					print('leu caracter - foi para L')
				elif c.lower() == '+':
					state = 'M'
					print('leu caracter + foi para M')
				elif c.lower() == '/':
					state = 'N'
					print('leu caracter / foi para N')
				elif c.lower() == '*':
					state = 'O'
					print('leu caracter * foi para O')
				elif c.lower() == '^':
					state = 'P'
					print('leu caracter ^ foi para P')
				elif c.lower() == '>':
					state = 'Q'
					print('leu caracter > foi para Q')
				elif c.lower() == '=':
					state = 'R'
					print('leu caracter = foi para R')
				elif c.lower() == '.':
					state = 'ER'
					print('leu caracter . foi para ER')
				elif c.lower() == ',':
					state = 'S'
					print('leu caracter , foi para S')
				elif c.lower() == ';':
					state = 'T'
					print('leu caracter ; foi para T')
				elif c.lower() == ':':
					state = 'RA'
					print('leu caracter : foi para RA')
				elif c.lower() == '(':
					state = 'U'
					print('leu caracter ( foi para U')
				elif c.lower() == ')':
					state = 'V'
					print('leu caracter ) foi para V')
				elif c.lower() == '[':
					state = 'W'
					print('leu caracter [ foi para W')
				elif c.lower() == ']':
					state = 'X'
					print('leu caracter ] foi para X')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'Y'
					print('leu caracter \n foi para Y')
				elif c.lower() == '\t':
					state = 'Y'
					print('leu caracter \t foi para Y')
				elif c.lower() == ' ':
					state = 'Y'
					print('leu caracter   foi para Y')
				elif c.lower() == '0':
					state = 'Z'
					print('leu caracter 0 foi para Z')
				elif c.lower() == '1':
					state = 'Z'
					print('leu caracter 1 foi para Z')
				elif c.lower() == '2':
					state = 'Z'
					print('leu caracter 2 foi para Z')
				elif c.lower() == '3':
					state = 'Z'
					print('leu caracter 3 foi para Z')
				elif c.lower() == '4':
					state = 'Z'
					print('leu caracter 4 foi para Z')
				elif c.lower() == '5':
					state = 'Z'
					print('leu caracter 5 foi para Z')
				elif c.lower() == '6':
					state = 'Z'
					print('leu caracter 6 foi para Z')
				elif c.lower() == '7':
					state = 'Z'
					print('leu caracter 7 foi para Z')
				elif c.lower() == '8':
					state = 'Z'
					print('leu caracter 8 foi para Z')
				elif c.lower() == '9':
					state = 'Z'
					print('leu caracter 9 foi para Z')
				elif c.lower() == '\'':
					state = 'AA'
					print('leu caracter \' foi para AA')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'L':
				print('Tratar retorno estado final L')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'M':
				print('Tratar retorno estado final M')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'N':
				print('Tratar retorno estado final N')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'O':
				print('Tratar retorno estado final O')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'P':
				print('Tratar retorno estado final P')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'R':
				print('Tratar retorno estado final R')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'ER':
				print('Tratar retorno estado final ER')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'S':
				print('Tratar retorno estado final S')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'T':
				print('Tratar retorno estado final T')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'RA':
				print('Tratar retorno estado final RA')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'U':
				print('Tratar retorno estado final U')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'V':
				print('Tratar retorno estado final V')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'X':
				print('Tratar retorno estado final X')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = True
			case 'B':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'AB'
					print('leu caracter t foi para AB')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AC':
				print('Tratar retorno estado final AC')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'C':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'D':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'AD'
					print('leu caracter h foi para AD')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'E':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'AE'
					print('leu caracter n foi para AE')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'F':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AF'
					print('leu caracter a foi para AF')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'AG'
					print('leu caracter i foi para AG')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'AH'
					print('leu caracter l foi para AH')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'G':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'AI'
					print('leu caracter n foi para AI')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'H':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'AJ'
					print('leu caracter r foi para AJ')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'I':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'AK'
					print('leu caracter e foi para AK')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'J':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'AL'
					print('leu caracter e foi para AL')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'K':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AM'
					print('leu caracter a foi para AM')
				elif c.lower() == 'b':
					state = 'AM'
					print('leu caracter b foi para AM')
				elif c.lower() == 'c':
					state = 'AM'
					print('leu caracter c foi para AM')
				elif c.lower() == 'd':
					state = 'AM'
					print('leu caracter d foi para AM')
				elif c.lower() == 'e':
					state = 'AM'
					print('leu caracter e foi para AM')
				elif c.lower() == 'f':
					state = 'AM'
					print('leu caracter f foi para AM')
				elif c.lower() == 'g':
					state = 'AM'
					print('leu caracter g foi para AM')
				elif c.lower() == 'h':
					state = 'AM'
					print('leu caracter h foi para AM')
				elif c.lower() == 'i':
					state = 'AM'
					print('leu caracter i foi para AM')
				elif c.lower() == 'j':
					state = 'AM'
					print('leu caracter j foi para AM')
				elif c.lower() == 'k':
					state = 'AM'
					print('leu caracter k foi para AM')
				elif c.lower() == 'l':
					state = 'AM'
					print('leu caracter l foi para AM')
				elif c.lower() == 'm':
					state = 'AM'
					print('leu caracter m foi para AM')
				elif c.lower() == 'n':
					state = 'AM'
					print('leu caracter n foi para AM')
				elif c.lower() == 'o':
					state = 'AM'
					print('leu caracter o foi para AM')
				elif c.lower() == 'p':
					state = 'AM'
					print('leu caracter p foi para AM')
				elif c.lower() == 'q':
					state = 'AM'
					print('leu caracter q foi para AM')
				elif c.lower() == 'r':
					state = 'AM'
					print('leu caracter r foi para AM')
				elif c.lower() == 's':
					state = 'AM'
					print('leu caracter s foi para AM')
				elif c.lower() == 't':
					state = 'AM'
					print('leu caracter t foi para AM')
				elif c.lower() == 'u':
					state = 'AM'
					print('leu caracter u foi para AM')
				elif c.lower() == 'v':
					state = 'AM'
					print('leu caracter v foi para AM')
				elif c.lower() == 'w':
					state = 'AM'
					print('leu caracter w foi para AM')
				elif c.lower() == 'x':
					state = 'AM'
					print('leu caracter x foi para AM')
				elif c.lower() == 'y':
					state = 'AM'
					print('leu caracter y foi para AM')
				elif c.lower() == 'z':
					state = 'AM'
					print('leu caracter z foi para AM')
				elif c.lower() == '_':
					state = 'AM'
					print('leu caracter _ foi para AM')
				elif c.lower() == '<':
					state = 'AM'
					print('leu caracter < foi para AM')
				elif c.lower() == '-':
					state = 'AN'
					print('leu caracter - foi para AN')
				elif c.lower() == '+':
					state = 'AM'
					print('leu caracter + foi para AM')
				elif c.lower() == '/':
					state = 'AM'
					print('leu caracter / foi para AM')
				elif c.lower() == '*':
					state = 'AM'
					print('leu caracter * foi para AM')
				elif c.lower() == '^':
					state = 'AM'
					print('leu caracter ^ foi para AM')
				elif c.lower() == '>':
					state = 'AO'
					print('leu caracter > foi para AO')
				elif c.lower() == '=':
					state = 'AP'
					print('leu caracter = foi para AP')
				elif c.lower() == '.':
					state = 'AM'
					print('leu caracter . foi para AM')
				elif c.lower() == ',':
					state = 'AM'
					print('leu caracter , foi para AM')
				elif c.lower() == ';':
					state = 'AM'
					print('leu caracter ; foi para AM')
				elif c.lower() == ':':
					state = 'AM'
					print('leu caracter : foi para AM')
				elif c.lower() == '(':
					state = 'AM'
					print('leu caracter ( foi para AM')
				elif c.lower() == ')':
					state = 'AM'
					print('leu caracter ) foi para AM')
				elif c.lower() == '[':
					state = 'AM'
					print('leu caracter [ foi para AM')
				elif c.lower() == ']':
					state = 'AM'
					print('leu caracter ] foi para AM')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AM'
					print('leu caracter \n foi para AM')
				elif c.lower() == '\t':
					state = 'AM'
					print('leu caracter \t foi para AM')
				elif c.lower() == ' ':
					state = 'AM'
					print('leu caracter   foi para AM')
				elif c.lower() == '0':
					state = 'AM'
					print('leu caracter 0 foi para AM')
				elif c.lower() == '1':
					state = 'AM'
					print('leu caracter 1 foi para AM')
				elif c.lower() == '2':
					state = 'AM'
					print('leu caracter 2 foi para AM')
				elif c.lower() == '3':
					state = 'AM'
					print('leu caracter 3 foi para AM')
				elif c.lower() == '4':
					state = 'AM'
					print('leu caracter 4 foi para AM')
				elif c.lower() == '5':
					state = 'AM'
					print('leu caracter 5 foi para AM')
				elif c.lower() == '6':
					state = 'AM'
					print('leu caracter 6 foi para AM')
				elif c.lower() == '7':
					state = 'AM'
					print('leu caracter 7 foi para AM')
				elif c.lower() == '8':
					state = 'AM'
					print('leu caracter 8 foi para AM')
				elif c.lower() == '9':
					state = 'AM'
					print('leu caracter 9 foi para AM')
				elif c.lower() == '\'':
					state = 'AM'
					print('leu caracter \' foi para AM')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AM':
				print('Tratar retorno estado final AM')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AO':
				print('Tratar retorno estado final AO')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AP':
				print('Tratar retorno estado final AP')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'Q':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AQ'
					print('leu caracter a foi para AQ')
				elif c.lower() == 'b':
					state = 'AQ'
					print('leu caracter b foi para AQ')
				elif c.lower() == 'c':
					state = 'AQ'
					print('leu caracter c foi para AQ')
				elif c.lower() == 'd':
					state = 'AQ'
					print('leu caracter d foi para AQ')
				elif c.lower() == 'e':
					state = 'AQ'
					print('leu caracter e foi para AQ')
				elif c.lower() == 'f':
					state = 'AQ'
					print('leu caracter f foi para AQ')
				elif c.lower() == 'g':
					state = 'AQ'
					print('leu caracter g foi para AQ')
				elif c.lower() == 'h':
					state = 'AQ'
					print('leu caracter h foi para AQ')
				elif c.lower() == 'i':
					state = 'AQ'
					print('leu caracter i foi para AQ')
				elif c.lower() == 'j':
					state = 'AQ'
					print('leu caracter j foi para AQ')
				elif c.lower() == 'k':
					state = 'AQ'
					print('leu caracter k foi para AQ')
				elif c.lower() == 'l':
					state = 'AQ'
					print('leu caracter l foi para AQ')
				elif c.lower() == 'm':
					state = 'AQ'
					print('leu caracter m foi para AQ')
				elif c.lower() == 'n':
					state = 'AQ'
					print('leu caracter n foi para AQ')
				elif c.lower() == 'o':
					state = 'AQ'
					print('leu caracter o foi para AQ')
				elif c.lower() == 'p':
					state = 'AQ'
					print('leu caracter p foi para AQ')
				elif c.lower() == 'q':
					state = 'AQ'
					print('leu caracter q foi para AQ')
				elif c.lower() == 'r':
					state = 'AQ'
					print('leu caracter r foi para AQ')
				elif c.lower() == 's':
					state = 'AQ'
					print('leu caracter s foi para AQ')
				elif c.lower() == 't':
					state = 'AQ'
					print('leu caracter t foi para AQ')
				elif c.lower() == 'u':
					state = 'AQ'
					print('leu caracter u foi para AQ')
				elif c.lower() == 'v':
					state = 'AQ'
					print('leu caracter v foi para AQ')
				elif c.lower() == 'w':
					state = 'AQ'
					print('leu caracter w foi para AQ')
				elif c.lower() == 'x':
					state = 'AQ'
					print('leu caracter x foi para AQ')
				elif c.lower() == 'y':
					state = 'AQ'
					print('leu caracter y foi para AQ')
				elif c.lower() == 'z':
					state = 'AQ'
					print('leu caracter z foi para AQ')
				elif c.lower() == '_':
					state = 'AQ'
					print('leu caracter _ foi para AQ')
				elif c.lower() == '<':
					state = 'AQ'
					print('leu caracter < foi para AQ')
				elif c.lower() == '-':
					state = 'AQ'
					print('leu caracter - foi para AQ')
				elif c.lower() == '+':
					state = 'AQ'
					print('leu caracter + foi para AQ')
				elif c.lower() == '/':
					state = 'AQ'
					print('leu caracter / foi para AQ')
				elif c.lower() == '*':
					state = 'AQ'
					print('leu caracter * foi para AQ')
				elif c.lower() == '^':
					state = 'AQ'
					print('leu caracter ^ foi para AQ')
				elif c.lower() == '>':
					state = 'AQ'
					print('leu caracter > foi para AQ')
				elif c.lower() == '=':
					state = 'AR'
					print('leu caracter = foi para AR')
				elif c.lower() == '.':
					state = 'AQ'
					print('leu caracter . foi para AQ')
				elif c.lower() == ',':
					state = 'AQ'
					print('leu caracter , foi para AQ')
				elif c.lower() == ';':
					state = 'AQ'
					print('leu caracter ; foi para AQ')
				elif c.lower() == ':':
					state = 'AQ'
					print('leu caracter : foi para AQ')
				elif c.lower() == '(':
					state = 'AQ'
					print('leu caracter ( foi para AQ')
				elif c.lower() == ')':
					state = 'AQ'
					print('leu caracter ) foi para AQ')
				elif c.lower() == '[':
					state = 'AQ'
					print('leu caracter [ foi para AQ')
				elif c.lower() == ']':
					state = 'AQ'
					print('leu caracter ] foi para AQ')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AQ'
					print('leu caracter \n foi para AQ')
				elif c.lower() == '\t':
					state = 'AQ'
					print('leu caracter \t foi para AQ')
				elif c.lower() == ' ':
					state = 'AQ'
					print('leu caracter   foi para AQ')
				elif c.lower() == '0':
					state = 'AQ'
					print('leu caracter 0 foi para AQ')
				elif c.lower() == '1':
					state = 'AQ'
					print('leu caracter 1 foi para AQ')
				elif c.lower() == '2':
					state = 'AQ'
					print('leu caracter 2 foi para AQ')
				elif c.lower() == '3':
					state = 'AQ'
					print('leu caracter 3 foi para AQ')
				elif c.lower() == '4':
					state = 'AQ'
					print('leu caracter 4 foi para AQ')
				elif c.lower() == '5':
					state = 'AQ'
					print('leu caracter 5 foi para AQ')
				elif c.lower() == '6':
					state = 'AQ'
					print('leu caracter 6 foi para AQ')
				elif c.lower() == '7':
					state = 'AQ'
					print('leu caracter 7 foi para AQ')
				elif c.lower() == '8':
					state = 'AQ'
					print('leu caracter 8 foi para AQ')
				elif c.lower() == '9':
					state = 'AQ'
					print('leu caracter 9 foi para AQ')
				elif c.lower() == '\'':
					state = 'AQ'
					print('leu caracter \' foi para AQ')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AQ':
				print('Tratar retorno estado final AQ')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AR':
				print('Tratar retorno estado final AR')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'Y':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AS'
					print('leu caracter a foi para AS')
				elif c.lower() == 'b':
					state = 'AS'
					print('leu caracter b foi para AS')
				elif c.lower() == 'c':
					state = 'AS'
					print('leu caracter c foi para AS')
				elif c.lower() == 'd':
					state = 'AS'
					print('leu caracter d foi para AS')
				elif c.lower() == 'e':
					state = 'AS'
					print('leu caracter e foi para AS')
				elif c.lower() == 'f':
					state = 'AS'
					print('leu caracter f foi para AS')
				elif c.lower() == 'g':
					state = 'AS'
					print('leu caracter g foi para AS')
				elif c.lower() == 'h':
					state = 'AS'
					print('leu caracter h foi para AS')
				elif c.lower() == 'i':
					state = 'AS'
					print('leu caracter i foi para AS')
				elif c.lower() == 'j':
					state = 'AS'
					print('leu caracter j foi para AS')
				elif c.lower() == 'k':
					state = 'AS'
					print('leu caracter k foi para AS')
				elif c.lower() == 'l':
					state = 'AS'
					print('leu caracter l foi para AS')
				elif c.lower() == 'm':
					state = 'AS'
					print('leu caracter m foi para AS')
				elif c.lower() == 'n':
					state = 'AS'
					print('leu caracter n foi para AS')
				elif c.lower() == 'o':
					state = 'AS'
					print('leu caracter o foi para AS')
				elif c.lower() == 'p':
					state = 'AS'
					print('leu caracter p foi para AS')
				elif c.lower() == 'q':
					state = 'AS'
					print('leu caracter q foi para AS')
				elif c.lower() == 'r':
					state = 'AS'
					print('leu caracter r foi para AS')
				elif c.lower() == 's':
					state = 'AS'
					print('leu caracter s foi para AS')
				elif c.lower() == 't':
					state = 'AS'
					print('leu caracter t foi para AS')
				elif c.lower() == 'u':
					state = 'AS'
					print('leu caracter u foi para AS')
				elif c.lower() == 'v':
					state = 'AS'
					print('leu caracter v foi para AS')
				elif c.lower() == 'w':
					state = 'AS'
					print('leu caracter w foi para AS')
				elif c.lower() == 'x':
					state = 'AS'
					print('leu caracter x foi para AS')
				elif c.lower() == 'y':
					state = 'AS'
					print('leu caracter y foi para AS')
				elif c.lower() == 'z':
					state = 'AS'
					print('leu caracter z foi para AS')
				elif c.lower() == '_':
					state = 'AS'
					print('leu caracter _ foi para AS')
				elif c.lower() == '<':
					state = 'AS'
					print('leu caracter < foi para AS')
				elif c.lower() == '-':
					state = 'AS'
					print('leu caracter - foi para AS')
				elif c.lower() == '+':
					state = 'AS'
					print('leu caracter + foi para AS')
				elif c.lower() == '/':
					state = 'AS'
					print('leu caracter / foi para AS')
				elif c.lower() == '*':
					state = 'AS'
					print('leu caracter * foi para AS')
				elif c.lower() == '^':
					state = 'AS'
					print('leu caracter ^ foi para AS')
				elif c.lower() == '>':
					state = 'AS'
					print('leu caracter > foi para AS')
				elif c.lower() == '=':
					state = 'AS'
					print('leu caracter = foi para AS')
				elif c.lower() == '.':
					state = 'AS'
					print('leu caracter . foi para AS')
				elif c.lower() == ',':
					state = 'AS'
					print('leu caracter , foi para AS')
				elif c.lower() == ';':
					state = 'AS'
					print('leu caracter ; foi para AS')
				elif c.lower() == ':':
					state = 'AS'
					print('leu caracter : foi para AS')
				elif c.lower() == '(':
					state = 'AS'
					print('leu caracter ( foi para AS')
				elif c.lower() == ')':
					state = 'AS'
					print('leu caracter ) foi para AS')
				elif c.lower() == '[':
					state = 'AS'
					print('leu caracter [ foi para AS')
				elif c.lower() == ']':
					state = 'AS'
					print('leu caracter ] foi para AS')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'Y'
					print('leu caracter \n foi para Y')
				elif c.lower() == '\t':
					state = 'Y'
					print('leu caracter \t foi para Y')
				elif c.lower() == ' ':
					state = 'Y'
					print('leu caracter   foi para Y')
				elif c.lower() == '0':
					state = 'AS'
					print('leu caracter 0 foi para AS')
				elif c.lower() == '1':
					state = 'AS'
					print('leu caracter 1 foi para AS')
				elif c.lower() == '2':
					state = 'AS'
					print('leu caracter 2 foi para AS')
				elif c.lower() == '3':
					state = 'AS'
					print('leu caracter 3 foi para AS')
				elif c.lower() == '4':
					state = 'AS'
					print('leu caracter 4 foi para AS')
				elif c.lower() == '5':
					state = 'AS'
					print('leu caracter 5 foi para AS')
				elif c.lower() == '6':
					state = 'AS'
					print('leu caracter 6 foi para AS')
				elif c.lower() == '7':
					state = 'AS'
					print('leu caracter 7 foi para AS')
				elif c.lower() == '8':
					state = 'AS'
					print('leu caracter 8 foi para AS')
				elif c.lower() == '9':
					state = 'AS'
					print('leu caracter 9 foi para AS')
				elif c.lower() == '\'':
					state = 'AS'
					print('leu caracter \' foi para AS')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AS':
				print('Tratar retorno estado final AS')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
			case 'Z':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AT'
					print('leu caracter a foi para AT')
				elif c.lower() == 'b':
					state = 'AT'
					print('leu caracter b foi para AT')
				elif c.lower() == 'c':
					state = 'AT'
					print('leu caracter c foi para AT')
				elif c.lower() == 'd':
					state = 'AT'
					print('leu caracter d foi para AT')
				elif c.lower() == 'e':
					state = 'AT'
					print('leu caracter e foi para AT')
				elif c.lower() == 'f':
					state = 'AT'
					print('leu caracter f foi para AT')
				elif c.lower() == 'g':
					state = 'AT'
					print('leu caracter g foi para AT')
				elif c.lower() == 'h':
					state = 'AT'
					print('leu caracter h foi para AT')
				elif c.lower() == 'i':
					state = 'AT'
					print('leu caracter i foi para AT')
				elif c.lower() == 'j':
					state = 'AT'
					print('leu caracter j foi para AT')
				elif c.lower() == 'k':
					state = 'AT'
					print('leu caracter k foi para AT')
				elif c.lower() == 'l':
					state = 'AT'
					print('leu caracter l foi para AT')
				elif c.lower() == 'm':
					state = 'AT'
					print('leu caracter m foi para AT')
				elif c.lower() == 'n':
					state = 'AT'
					print('leu caracter n foi para AT')
				elif c.lower() == 'o':
					state = 'AT'
					print('leu caracter o foi para AT')
				elif c.lower() == 'p':
					state = 'AT'
					print('leu caracter p foi para AT')
				elif c.lower() == 'q':
					state = 'AT'
					print('leu caracter q foi para AT')
				elif c.lower() == 'r':
					state = 'AT'
					print('leu caracter r foi para AT')
				elif c.lower() == 's':
					state = 'AT'
					print('leu caracter s foi para AT')
				elif c.lower() == 't':
					state = 'AT'
					print('leu caracter t foi para AT')
				elif c.lower() == 'u':
					state = 'AT'
					print('leu caracter u foi para AT')
				elif c.lower() == 'v':
					state = 'AT'
					print('leu caracter v foi para AT')
				elif c.lower() == 'w':
					state = 'AT'
					print('leu caracter w foi para AT')
				elif c.lower() == 'x':
					state = 'AT'
					print('leu caracter x foi para AT')
				elif c.lower() == 'y':
					state = 'AT'
					print('leu caracter y foi para AT')
				elif c.lower() == 'z':
					state = 'AT'
					print('leu caracter z foi para AT')
				elif c.lower() == '_':
					state = 'AT'
					print('leu caracter _ foi para AT')
				elif c.lower() == '<':
					state = 'AT'
					print('leu caracter < foi para AT')
				elif c.lower() == '-':
					state = 'AT'
					print('leu caracter - foi para AT')
				elif c.lower() == '+':
					state = 'AT'
					print('leu caracter + foi para AT')
				elif c.lower() == '/':
					state = 'AT'
					print('leu caracter / foi para AT')
				elif c.lower() == '*':
					state = 'AT'
					print('leu caracter * foi para AT')
				elif c.lower() == '^':
					state = 'AT'
					print('leu caracter ^ foi para AT')
				elif c.lower() == '>':
					state = 'AT'
					print('leu caracter > foi para AT')
				elif c.lower() == '=':
					state = 'AT'
					print('leu caracter = foi para AT')
				elif c.lower() == '.':
					state = 'AU'
					print('leu caracter . foi para AU')
				elif c.lower() == ',':
					state = 'AT'
					print('leu caracter , foi para AT')
				elif c.lower() == ';':
					state = 'AT'
					print('leu caracter ; foi para AT')
				elif c.lower() == ':':
					state = 'AT'
					print('leu caracter : foi para AT')
				elif c.lower() == '(':
					state = 'AT'
					print('leu caracter ( foi para AT')
				elif c.lower() == ')':
					state = 'AT'
					print('leu caracter ) foi para AT')
				elif c.lower() == '[':
					state = 'AT'
					print('leu caracter [ foi para AT')
				elif c.lower() == ']':
					state = 'AT'
					print('leu caracter ] foi para AT')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AT'
					print('leu caracter \n foi para AT')
				elif c.lower() == '\t':
					state = 'AT'
					print('leu caracter \t foi para AT')
				elif c.lower() == ' ':
					state = 'AT'
					print('leu caracter   foi para AT')
				elif c.lower() == '0':
					state = 'Z'
					print('leu caracter 0 foi para Z')
				elif c.lower() == '1':
					state = 'Z'
					print('leu caracter 1 foi para Z')
				elif c.lower() == '2':
					state = 'Z'
					print('leu caracter 2 foi para Z')
				elif c.lower() == '3':
					state = 'Z'
					print('leu caracter 3 foi para Z')
				elif c.lower() == '4':
					state = 'Z'
					print('leu caracter 4 foi para Z')
				elif c.lower() == '5':
					state = 'Z'
					print('leu caracter 5 foi para Z')
				elif c.lower() == '6':
					state = 'Z'
					print('leu caracter 6 foi para Z')
				elif c.lower() == '7':
					state = 'Z'
					print('leu caracter 7 foi para Z')
				elif c.lower() == '8':
					state = 'Z'
					print('leu caracter 8 foi para Z')
				elif c.lower() == '9':
					state = 'Z'
					print('leu caracter 9 foi para Z')
				elif c.lower() == '\'':
					state = 'AT'
					print('leu caracter \' foi para AT')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AT':
				print('Tratar retorno estado final AT')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AA':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AV'
					print('leu caracter a foi para AV')
				elif c.lower() == 'b':
					state = 'AV'
					print('leu caracter b foi para AV')
				elif c.lower() == 'c':
					state = 'AV'
					print('leu caracter c foi para AV')
				elif c.lower() == 'd':
					state = 'AV'
					print('leu caracter d foi para AV')
				elif c.lower() == 'e':
					state = 'AV'
					print('leu caracter e foi para AV')
				elif c.lower() == 'f':
					state = 'AV'
					print('leu caracter f foi para AV')
				elif c.lower() == 'g':
					state = 'AV'
					print('leu caracter g foi para AV')
				elif c.lower() == 'h':
					state = 'AV'
					print('leu caracter h foi para AV')
				elif c.lower() == 'i':
					state = 'AV'
					print('leu caracter i foi para AV')
				elif c.lower() == 'j':
					state = 'AV'
					print('leu caracter j foi para AV')
				elif c.lower() == 'k':
					state = 'AV'
					print('leu caracter k foi para AV')
				elif c.lower() == 'l':
					state = 'AV'
					print('leu caracter l foi para AV')
				elif c.lower() == 'm':
					state = 'AV'
					print('leu caracter m foi para AV')
				elif c.lower() == 'n':
					state = 'AV'
					print('leu caracter n foi para AV')
				elif c.lower() == 'o':
					state = 'AV'
					print('leu caracter o foi para AV')
				elif c.lower() == 'p':
					state = 'AV'
					print('leu caracter p foi para AV')
				elif c.lower() == 'q':
					state = 'AV'
					print('leu caracter q foi para AV')
				elif c.lower() == 'r':
					state = 'AV'
					print('leu caracter r foi para AV')
				elif c.lower() == 's':
					state = 'AV'
					print('leu caracter s foi para AV')
				elif c.lower() == 't':
					state = 'AV'
					print('leu caracter t foi para AV')
				elif c.lower() == 'u':
					state = 'AV'
					print('leu caracter u foi para AV')
				elif c.lower() == 'v':
					state = 'AV'
					print('leu caracter v foi para AV')
				elif c.lower() == 'w':
					state = 'AV'
					print('leu caracter w foi para AV')
				elif c.lower() == 'x':
					state = 'AV'
					print('leu caracter x foi para AV')
				elif c.lower() == 'y':
					state = 'AV'
					print('leu caracter y foi para AV')
				elif c.lower() == 'z':
					state = 'AV'
					print('leu caracter z foi para AV')
				elif c.lower() == '_':
					state = 'ER'
					print('leu caracter _ foi para ER')
				elif c.lower() == '<':
					state = 'ER'
					print('leu caracter < foi para ER')
				elif c.lower() == '-':
					state = 'ER'
					print('leu caracter - foi para ER')
				elif c.lower() == '+':
					state = 'ER'
					print('leu caracter + foi para ER')
				elif c.lower() == '/':
					state = 'ER'
					print('leu caracter / foi para ER')
				elif c.lower() == '*':
					state = 'ER'
					print('leu caracter * foi para ER')
				elif c.lower() == '^':
					state = 'ER'
					print('leu caracter ^ foi para ER')
				elif c.lower() == '>':
					state = 'ER'
					print('leu caracter > foi para ER')
				elif c.lower() == '=':
					state = 'ER'
					print('leu caracter = foi para ER')
				elif c.lower() == '.':
					state = 'ER'
					print('leu caracter . foi para ER')
				elif c.lower() == ',':
					state = 'ER'
					print('leu caracter , foi para ER')
				elif c.lower() == ';':
					state = 'ER'
					print('leu caracter ; foi para ER')
				elif c.lower() == ':':
					state = 'ER'
					print('leu caracter : foi para ER')
				elif c.lower() == '(':
					state = 'ER'
					print('leu caracter ( foi para ER')
				elif c.lower() == ')':
					state = 'ER'
					print('leu caracter ) foi para ER')
				elif c.lower() == '[':
					state = 'ER'
					print('leu caracter [ foi para ER')
				elif c.lower() == ']':
					state = 'ER'
					print('leu caracter ] foi para ER')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'ER'
					print('leu caracter \n foi para ER')
				elif c.lower() == '\t':
					state = 'ER'
					print('leu caracter \t foi para ER')
				elif c.lower() == ' ':
					state = 'ER'
					print('leu caracter   foi para ER')
				elif c.lower() == '0':
					state = 'ER'
					print('leu caracter 0 foi para ER')
				elif c.lower() == '1':
					state = 'ER'
					print('leu caracter 1 foi para ER')
				elif c.lower() == '2':
					state = 'ER'
					print('leu caracter 2 foi para ER')
				elif c.lower() == '3':
					state = 'ER'
					print('leu caracter 3 foi para ER')
				elif c.lower() == '4':
					state = 'ER'
					print('leu caracter 4 foi para ER')
				elif c.lower() == '5':
					state = 'ER'
					print('leu caracter 5 foi para ER')
				elif c.lower() == '6':
					state = 'ER'
					print('leu caracter 6 foi para ER')
				elif c.lower() == '7':
					state = 'ER'
					print('leu caracter 7 foi para ER')
				elif c.lower() == '8':
					state = 'ER'
					print('leu caracter 8 foi para ER')
				elif c.lower() == '9':
					state = 'ER'
					print('leu caracter 9 foi para ER')
				elif c.lower() == '\'':
					state = 'ER'
					print('leu caracter \' foi para ER')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AB':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'AW'
					print('leu caracter e foi para AW')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AD':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AY'
					print('leu caracter a foi para AY')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AE':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AY'
					print('leu caracter a foi para AY')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'AX'
					print('leu caracter q foi para AX')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'AZ'
					print('leu caracter t foi para AZ')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AF':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'BA'
					print('leu caracter c foi para BA')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AG':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'BB'
					print('leu caracter m foi para BB')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AH':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'BC'
					print('leu caracter o foi para BC')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AI':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'BD'
					print('leu caracter i foi para BD')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'BE'
					print('leu caracter t foi para BE')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AJ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'BF'
					print('leu caracter o foi para BF')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AK':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'BG'
					print('leu caracter p foi para BG')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AL':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'BH'
					print('leu caracter n foi para BH')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'BI'
					print('leu caracter < foi para BI')
				elif c.lower() == '-':
					state = 'BI'
					print('leu caracter - foi para BI')
				elif c.lower() == '+':
					state = 'BI'
					print('leu caracter + foi para BI')
				elif c.lower() == '/':
					state = 'BI'
					print('leu caracter / foi para BI')
				elif c.lower() == '*':
					state = 'BI'
					print('leu caracter * foi para BI')
				elif c.lower() == '^':
					state = 'BI'
					print('leu caracter ^ foi para BI')
				elif c.lower() == '>':
					state = 'BI'
					print('leu caracter > foi para BI')
				elif c.lower() == '=':
					state = 'BI'
					print('leu caracter = foi para BI')
				elif c.lower() == '.':
					state = 'BI'
					print('leu caracter . foi para BI')
				elif c.lower() == ',':
					state = 'BI'
					print('leu caracter , foi para BI')
				elif c.lower() == ';':
					state = 'BI'
					print('leu caracter ; foi para BI')
				elif c.lower() == ':':
					state = 'BI'
					print('leu caracter : foi para BI')
				elif c.lower() == '(':
					state = 'BI'
					print('leu caracter ( foi para BI')
				elif c.lower() == ')':
					state = 'BI'
					print('leu caracter ) foi para BI')
				elif c.lower() == '[':
					state = 'BI'
					print('leu caracter [ foi para BI')
				elif c.lower() == ']':
					state = 'BI'
					print('leu caracter ] foi para BI')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'BI'
					print('leu caracter \n foi para BI')
				elif c.lower() == '\t':
					state = 'BI'
					print('leu caracter \t foi para BI')
				elif c.lower() == ' ':
					state = 'BI'
					print('leu caracter   foi para BI')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'BI'
					print('leu caracter \' foi para BI')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BI':
				print('Tratar retorno estado final BI')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AN':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == '-':
					state = 'BJ'
					print('leu caracter - foi para BJ')
				else:
					print('Tratar retorno estado final BI')
					print(f"Identificador montado {id}")
					state = 'A'
					lerProx = False
					if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
						f.seek(f.tell()-1)
						return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
					elif c in ['\n', '\t', ' ',';',')','+']:
						return Token(id,'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AU':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'ER'
					print('leu caracter a foi para ER')
				elif c.lower() == 'b':
					state = 'ER'
					print('leu caracter b foi para ER')
				elif c.lower() == 'c':
					state = 'ER'
					print('leu caracter c foi para ER')
				elif c.lower() == 'd':
					state = 'ER'
					print('leu caracter d foi para ER')
				elif c.lower() == 'e':
					state = 'ER'
					print('leu caracter e foi para ER')
				elif c.lower() == 'f':
					state = 'ER'
					print('leu caracter f foi para ER')
				elif c.lower() == 'g':
					state = 'ER'
					print('leu caracter g foi para ER')
				elif c.lower() == 'h':
					state = 'ER'
					print('leu caracter h foi para ER')
				elif c.lower() == 'i':
					state = 'ER'
					print('leu caracter i foi para ER')
				elif c.lower() == 'j':
					state = 'ER'
					print('leu caracter j foi para ER')
				elif c.lower() == 'k':
					state = 'ER'
					print('leu caracter k foi para ER')
				elif c.lower() == 'l':
					state = 'ER'
					print('leu caracter l foi para ER')
				elif c.lower() == 'm':
					state = 'ER'
					print('leu caracter m foi para ER')
				elif c.lower() == 'n':
					state = 'ER'
					print('leu caracter n foi para ER')
				elif c.lower() == 'o':
					state = 'ER'
					print('leu caracter o foi para ER')
				elif c.lower() == 'p':
					state = 'ER'
					print('leu caracter p foi para ER')
				elif c.lower() == 'q':
					state = 'ER'
					print('leu caracter q foi para ER')
				elif c.lower() == 'r':
					state = 'ER'
					print('leu caracter r foi para ER')
				elif c.lower() == 's':
					state = 'ER'
					print('leu caracter s foi para ER')
				elif c.lower() == 't':
					state = 'ER'
					print('leu caracter t foi para ER')
				elif c.lower() == 'u':
					state = 'ER'
					print('leu caracter u foi para ER')
				elif c.lower() == 'v':
					state = 'ER'
					print('leu caracter v foi para ER')
				elif c.lower() == 'w':
					state = 'ER'
					print('leu caracter w foi para ER')
				elif c.lower() == 'x':
					state = 'ER'
					print('leu caracter x foi para ER')
				elif c.lower() == 'y':
					state = 'ER'
					print('leu caracter y foi para ER')
				elif c.lower() == 'z':
					state = 'ER'
					print('leu caracter z foi para ER')
				elif c.lower() == '_':
					state = 'ER'
					print('leu caracter _ foi para ER')
				elif c.lower() == '<':
					state = 'ER'
					print('leu caracter < foi para ER')
				elif c.lower() == '-':
					state = 'ER'
					print('leu caracter - foi para ER')
				elif c.lower() == '+':
					state = 'ER'
					print('leu caracter + foi para ER')
				elif c.lower() == '/':
					state = 'ER'
					print('leu caracter / foi para ER')
				elif c.lower() == '*':
					state = 'ER'
					print('leu caracter * foi para ER')
				elif c.lower() == '^':
					state = 'ER'
					print('leu caracter ^ foi para ER')
				elif c.lower() == '>':
					state = 'ER'
					print('leu caracter > foi para ER')
				elif c.lower() == '=':
					state = 'ER'
					print('leu caracter = foi para ER')
				elif c.lower() == '.':
					state = 'ER'
					print('leu caracter . foi para ER')
				elif c.lower() == ',':
					state = 'ER'
					print('leu caracter , foi para ER')
				elif c.lower() == ';':
					state = 'ER'
					print('leu caracter ; foi para ER')
				elif c.lower() == ':':
					state = 'ER'
					print('leu caracter : foi para ER')
				elif c.lower() == '(':
					state = 'ER'
					print('leu caracter ( foi para ER')
				elif c.lower() == ')':
					state = 'ER'
					print('leu caracter ) foi para ER')
				elif c.lower() == '[':
					state = 'ER'
					print('leu caracter [ foi para ER')
				elif c.lower() == ']':
					state = 'ER'
					print('leu caracter ] foi para ER')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'ER'
					print('leu caracter \n foi para ER')
				elif c.lower() == '\t':
					state = 'ER'
					print('leu caracter \t foi para ER')
				elif c.lower() == ' ':
					state = 'ER'
					print('leu caracter   foi para ER')
				elif c.lower() == '0':
					state = 'BK'
					print('leu caracter 0 foi para BK')
				elif c.lower() == '1':
					state = 'BK'
					print('leu caracter 1 foi para BK')
				elif c.lower() == '2':
					state = 'BK'
					print('leu caracter 2 foi para BK')
				elif c.lower() == '3':
					state = 'BK'
					print('leu caracter 3 foi para BK')
				elif c.lower() == '4':
					state = 'BK'
					print('leu caracter 4 foi para BK')
				elif c.lower() == '5':
					state = 'BK'
					print('leu caracter 5 foi para BK')
				elif c.lower() == '6':
					state = 'BK'
					print('leu caracter 6 foi para BK')
				elif c.lower() == '7':
					state = 'BK'
					print('leu caracter 7 foi para BK')
				elif c.lower() == '8':
					state = 'BK'
					print('leu caracter 8 foi para BK')
				elif c.lower() == '9':
					state = 'BK'
					print('leu caracter 9 foi para BK')
				elif c.lower() == '\'':
					state = 'ER'
					print('leu caracter \' foi para ER')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AV':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'ER'
					print('leu caracter a foi para ER')
				elif c.lower() == 'b':
					state = 'ER'
					print('leu caracter b foi para ER')
				elif c.lower() == 'c':
					state = 'ER'
					print('leu caracter c foi para ER')
				elif c.lower() == 'd':
					state = 'ER'
					print('leu caracter d foi para ER')
				elif c.lower() == 'e':
					state = 'ER'
					print('leu caracter e foi para ER')
				elif c.lower() == 'f':
					state = 'ER'
					print('leu caracter f foi para ER')
				elif c.lower() == 'g':
					state = 'ER'
					print('leu caracter g foi para ER')
				elif c.lower() == 'h':
					state = 'ER'
					print('leu caracter h foi para ER')
				elif c.lower() == 'i':
					state = 'ER'
					print('leu caracter i foi para ER')
				elif c.lower() == 'j':
					state = 'ER'
					print('leu caracter j foi para ER')
				elif c.lower() == 'k':
					state = 'ER'
					print('leu caracter k foi para ER')
				elif c.lower() == 'l':
					state = 'ER'
					print('leu caracter l foi para ER')
				elif c.lower() == 'm':
					state = 'ER'
					print('leu caracter m foi para ER')
				elif c.lower() == 'n':
					state = 'ER'
					print('leu caracter n foi para ER')
				elif c.lower() == 'o':
					state = 'ER'
					print('leu caracter o foi para ER')
				elif c.lower() == 'p':
					state = 'ER'
					print('leu caracter p foi para ER')
				elif c.lower() == 'q':
					state = 'ER'
					print('leu caracter q foi para ER')
				elif c.lower() == 'r':
					state = 'ER'
					print('leu caracter r foi para ER')
				elif c.lower() == 's':
					state = 'ER'
					print('leu caracter s foi para ER')
				elif c.lower() == 't':
					state = 'ER'
					print('leu caracter t foi para ER')
				elif c.lower() == 'u':
					state = 'ER'
					print('leu caracter u foi para ER')
				elif c.lower() == 'v':
					state = 'ER'
					print('leu caracter v foi para ER')
				elif c.lower() == 'w':
					state = 'ER'
					print('leu caracter w foi para ER')
				elif c.lower() == 'x':
					state = 'ER'
					print('leu caracter x foi para ER')
				elif c.lower() == 'y':
					state = 'ER'
					print('leu caracter y foi para ER')
				elif c.lower() == 'z':
					state = 'ER'
					print('leu caracter z foi para ER')
				elif c.lower() == '_':
					state = 'ER'
					print('leu caracter _ foi para ER')
				elif c.lower() == '<':
					state = 'ER'
					print('leu caracter < foi para ER')
				elif c.lower() == '-':
					state = 'ER'
					print('leu caracter - foi para ER')
				elif c.lower() == '+':
					state = 'ER'
					print('leu caracter + foi para ER')
				elif c.lower() == '/':
					state = 'ER'
					print('leu caracter / foi para ER')
				elif c.lower() == '*':
					state = 'ER'
					print('leu caracter * foi para ER')
				elif c.lower() == '^':
					state = 'ER'
					print('leu caracter ^ foi para ER')
				elif c.lower() == '>':
					state = 'ER'
					print('leu caracter > foi para ER')
				elif c.lower() == '=':
					state = 'ER'
					print('leu caracter = foi para ER')
				elif c.lower() == '.':
					state = 'ER'
					print('leu caracter . foi para ER')
				elif c.lower() == ',':
					state = 'ER'
					print('leu caracter , foi para ER')
				elif c.lower() == ';':
					state = 'ER'
					print('leu caracter ; foi para ER')
				elif c.lower() == ':':
					state = 'ER'
					print('leu caracter : foi para ER')
				elif c.lower() == '(':
					state = 'ER'
					print('leu caracter ( foi para ER')
				elif c.lower() == ')':
					state = 'ER'
					print('leu caracter ) foi para ER')
				elif c.lower() == '[':
					state = 'ER'
					print('leu caracter [ foi para ER')
				elif c.lower() == ']':
					state = 'ER'
					print('leu caracter ] foi para ER')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'ER'
					print('leu caracter \n foi para ER')
				elif c.lower() == '\t':
					state = 'ER'
					print('leu caracter \t foi para ER')
				elif c.lower() == ' ':
					state = 'ER'
					print('leu caracter   foi para ER')
				elif c.lower() == '0':
					state = 'ER'
					print('leu caracter 0 foi para ER')
				elif c.lower() == '1':
					state = 'ER'
					print('leu caracter 1 foi para ER')
				elif c.lower() == '2':
					state = 'ER'
					print('leu caracter 2 foi para ER')
				elif c.lower() == '3':
					state = 'ER'
					print('leu caracter 3 foi para ER')
				elif c.lower() == '4':
					state = 'ER'
					print('leu caracter 4 foi para ER')
				elif c.lower() == '5':
					state = 'ER'
					print('leu caracter 5 foi para ER')
				elif c.lower() == '6':
					state = 'ER'
					print('leu caracter 6 foi para ER')
				elif c.lower() == '7':
					state = 'ER'
					print('leu caracter 7 foi para ER')
				elif c.lower() == '8':
					state = 'ER'
					print('leu caracter 8 foi para ER')
				elif c.lower() == '9':
					state = 'ER'
					print('leu caracter 9 foi para ER')
				elif c.lower() == '\'':
					state = 'BL'
					print('leu caracter \' foi para BL')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BL':
				print('Tratar retorno estado final BL')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AW':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'BM'
					print('leu caracter < foi para BM')
				elif c.lower() == '-':
					state = 'BM'
					print('leu caracter - foi para BM')
				elif c.lower() == '+':
					state = 'BM'
					print('leu caracter + foi para BM')
				elif c.lower() == '/':
					state = 'BM'
					print('leu caracter / foi para BM')
				elif c.lower() == '*':
					state = 'BM'
					print('leu caracter * foi para BM')
				elif c.lower() == '^':
					state = 'BM'
					print('leu caracter ^ foi para BM')
				elif c.lower() == '>':
					state = 'BM'
					print('leu caracter > foi para BM')
				elif c.lower() == '=':
					state = 'BM'
					print('leu caracter = foi para BM')
				elif c.lower() == '.':
					state = 'BM'
					print('leu caracter . foi para BM')
				elif c.lower() == ',':
					state = 'BM'
					print('leu caracter , foi para BM')
				elif c.lower() == ';':
					state = 'BM'
					print('leu caracter ; foi para BM')
				elif c.lower() == ':':
					state = 'BM'
					print('leu caracter : foi para BM')
				elif c.lower() == '(':
					state = 'BM'
					print('leu caracter ( foi para BM')
				elif c.lower() == ')':
					state = 'BM'
					print('leu caracter ) foi para BM')
				elif c.lower() == '[':
					state = 'BM'
					print('leu caracter [ foi para BM')
				elif c.lower() == ']':
					state = 'BM'
					print('leu caracter ] foi para BM')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'BM'
					print('leu caracter \n foi para BM')
				elif c.lower() == '\t':
					state = 'BM'
					print('leu caracter \t foi para BM')
				elif c.lower() == ' ':
					state = 'BM'
					print('leu caracter   foi para BM')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'BM'
					print('leu caracter \' foi para BM')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BM':
				print('Tratar retorno estado final BM')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AY':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'BN'
					print('leu caracter r foi para BN')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AX':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'BO'
					print('leu caracter u foi para BO')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AZ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AZZ'
					print('leu caracter a foi para AZZ')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AZZ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'BP'
					print('leu caracter o foi para BP')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'C'
					print('leu caracter < foi para C')
				elif c.lower() == '-':
					state = 'C'
					print('leu caracter - foi para C')
				elif c.lower() == '+':
					state = 'C'
					print('leu caracter + foi para C')
				elif c.lower() == '/':
					state = 'C'
					print('leu caracter / foi para C')
				elif c.lower() == '*':
					state = 'C'
					print('leu caracter * foi para C')
				elif c.lower() == '^':
					state = 'C'
					print('leu caracter ^ foi para C')
				elif c.lower() == '>':
					state = 'C'
					print('leu caracter > foi para C')
				elif c.lower() == '=':
					state = 'C'
					print('leu caracter = foi para C')
				elif c.lower() == '.':
					state = 'C'
					print('leu caracter . foi para C')
				elif c.lower() == ',':
					state = 'C'
					print('leu caracter , foi para C')
				elif c.lower() == ';':
					state = 'C'
					print('leu caracter ; foi para C')
				elif c.lower() == '(':
					state = 'C'
					print('leu caracter ( foi para C')
				elif c.lower() == ')':
					state = 'C'
					print('leu caracter ) foi para C')
				elif c.lower() == '[':
					state = 'C'
					print('leu caracter [ foi para C')
				elif c.lower() == ']':
					state = 'X'
					print('leu caracter ] foi para X')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'C'
					print('leu caracter \n foi para C')
				elif c.lower() == '\t':
					state = 'C'
					print('leu caracter \t foi para C')
				elif c.lower() == ' ':
					state = 'C'
					print('leu caracter   foi para C')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'C'
					print('leu caracter \' foi para C')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BA':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'BQ'
					print('leu caracter a foi para BQ')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BB':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'BR'
					print('leu caracter < foi para BR')
				elif c.lower() == '-':
					state = 'BR'
					print('leu caracter - foi para BR')
				elif c.lower() == '+':
					state = 'BR'
					print('leu caracter + foi para BR')
				elif c.lower() == '/':
					state = 'BR'
					print('leu caracter / foi para BR')
				elif c.lower() == '*':
					state = 'BR'
					print('leu caracter * foi para BR')
				elif c.lower() == '^':
					state = 'BR'
					print('leu caracter ^ foi para BR')
				elif c.lower() == '>':
					state = 'BR'
					print('leu caracter > foi para BR')
				elif c.lower() == '=':
					state = 'BR'
					print('leu caracter = foi para BR')
				elif c.lower() == '.':
					state = 'BR'
					print('leu caracter . foi para BR')
				elif c.lower() == ',':
					state = 'BR'
					print('leu caracter , foi para BR')
				elif c.lower() == ';':
					state = 'BR'
					print('leu caracter ; foi para BR')
				elif c.lower() == ':':
					state = 'BR'
					print('leu caracter : foi para BR')
				elif c.lower() == '(':
					state = 'BR'
					print('leu caracter ( foi para BR')
				elif c.lower() == ')':
					state = 'BR'
					print('leu caracter ) foi para BR')
				elif c.lower() == '[':
					state = 'BR'
					print('leu caracter [ foi para BR')
				elif c.lower() == ']':
					state = 'BR'
					print('leu caracter ] foi para BR')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'BR'
					print('leu caracter \n foi para BR')
				elif c.lower() == '\t':
					state = 'BR'
					print('leu caracter \t foi para BR')
				elif c.lower() == ' ':
					state = 'BR'
					print('leu caracter   foi para BR')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'BR'
					print('leu caracter \' foi para BR')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BR':
				print('Tratar retorno estado final BR')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'BC':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'BS'
					print('leu caracter a foi para BS')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BD':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'BT'
					print('leu caracter c foi para BT')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BE':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'BU'
					print('leu caracter < foi para BU')
				elif c.lower() == '-':
					state = 'BU'
					print('leu caracter - foi para BU')
				elif c.lower() == '+':
					state = 'BU'
					print('leu caracter + foi para BU')
				elif c.lower() == '/':
					state = 'BU'
					print('leu caracter / foi para BU')
				elif c.lower() == '*':
					state = 'BU'
					print('leu caracter * foi para BU')
				elif c.lower() == '^':
					state = 'BU'
					print('leu caracter ^ foi para BU')
				elif c.lower() == '>':
					state = 'BU'
					print('leu caracter > foi para BU')
				elif c.lower() == '=':
					state = 'BU'
					print('leu caracter = foi para BU')
				elif c.lower() == '.':
					state = 'BU'
					print('leu caracter . foi para BU')
				elif c.lower() == ',':
					state = 'BU'
					print('leu caracter , foi para BU')
				elif c.lower() == ';':
					state = 'BU'
					print('leu caracter ; foi para BU')
				elif c.lower() == ':':
					state = 'BU'
					print('leu caracter : foi para BU')
				elif c.lower() == '(':
					state = 'BU'
					print('leu caracter ( foi para BU')
				elif c.lower() == ')':
					state = 'BU'
					print('leu caracter ) foi para BU')
				elif c.lower() == '[':
					state = 'BU'
					print('leu caracter [ foi para BU')
				elif c.lower() == ']':
					state = 'BU'
					print('leu caracter ] foi para BU')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'BU'
					print('leu caracter \n foi para BU')
				elif c.lower() == '\t':
					state = 'BU'
					print('leu caracter \t foi para BU')
				elif c.lower() == ' ':
					state = 'BU'
					print('leu caracter   foi para BU')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'BU'
					print('leu caracter \' foi para BU')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BU':
				print('Tratar retorno estado final BU')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'BF':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'BV'
					print('leu caracter g foi para BV')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BG':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'BW'
					print('leu caracter i foi para BW')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BH':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'BX'
					print('leu caracter o foi para BX')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BJ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'BY'
					print('leu caracter a foi para BY')
				elif c.lower() == 'b':
					state = 'BY'
					print('leu caracter b foi para BY')
				elif c.lower() == 'c':
					state = 'BY'
					print('leu caracter c foi para BY')
				elif c.lower() == 'd':
					state = 'BY'
					print('leu caracter d foi para BY')
				elif c.lower() == 'e':
					state = 'BY'
					print('leu caracter e foi para BY')
				elif c.lower() == 'f':
					state = 'BY'
					print('leu caracter f foi para BY')
				elif c.lower() == 'g':
					state = 'BY'
					print('leu caracter g foi para BY')
				elif c.lower() == 'h':
					state = 'BY'
					print('leu caracter h foi para BY')
				elif c.lower() == 'i':
					state = 'BY'
					print('leu caracter i foi para BY')
				elif c.lower() == 'j':
					state = 'BY'
					print('leu caracter j foi para BY')
				elif c.lower() == 'k':
					state = 'BY'
					print('leu caracter k foi para BY')
				elif c.lower() == 'l':
					state = 'BY'
					print('leu caracter l foi para BY')
				elif c.lower() == 'm':
					state = 'BY'
					print('leu caracter m foi para BY')
				elif c.lower() == 'n':
					state = 'BY'
					print('leu caracter n foi para BY')
				elif c.lower() == 'o':
					state = 'BY'
					print('leu caracter o foi para BY')
				elif c.lower() == 'p':
					state = 'BY'
					print('leu caracter p foi para BY')
				elif c.lower() == 'q':
					state = 'BY'
					print('leu caracter q foi para BY')
				elif c.lower() == 'r':
					state = 'BY'
					print('leu caracter r foi para BY')
				elif c.lower() == 's':
					state = 'BY'
					print('leu caracter s foi para BY')
				elif c.lower() == 't':
					state = 'BY'
					print('leu caracter t foi para BY')
				elif c.lower() == 'u':
					state = 'BY'
					print('leu caracter u foi para BY')
				elif c.lower() == 'v':
					state = 'BY'
					print('leu caracter v foi para BY')
				elif c.lower() == 'w':
					state = 'BY'
					print('leu caracter w foi para BY')
				elif c.lower() == 'x':
					state = 'BY'
					print('leu caracter x foi para BY')
				elif c.lower() == 'y':
					state = 'BY'
					print('leu caracter y foi para BY')
				elif c.lower() == 'z':
					state = 'BY'
					print('leu caracter z foi para BY')
				elif c.lower() == '_':
					state = 'BY'
					print('leu caracter _ foi para BY')
				elif c.lower() == '<':
					state = 'BY'
					print('leu caracter < foi para BY')
				elif c.lower() == '-':
					state = 'BY'
					print('leu caracter - foi para BY')
				elif c.lower() == '+':
					state = 'BY'
					print('leu caracter + foi para BY')
				elif c.lower() == '/':
					state = 'BY'
					print('leu caracter / foi para BY')
				elif c.lower() == '*':
					state = 'BY'
					print('leu caracter * foi para BY')
				elif c.lower() == '^':
					state = 'BY'
					print('leu caracter ^ foi para BY')
				elif c.lower() == '>':
					state = 'BY'
					print('leu caracter > foi para BY')
				elif c.lower() == '=':
					state = 'BY'
					print('leu caracter = foi para BY')
				elif c.lower() == '.':
					state = 'BY'
					print('leu caracter . foi para BY')
				elif c.lower() == ',':
					state = 'BY'
					print('leu caracter , foi para BY')
				elif c.lower() == ';':
					state = 'BY'
					print('leu caracter ; foi para BY')
				elif c.lower() == ':':
					state = 'BY'
					print('leu caracter : foi para BY')
				elif c.lower() == '(':
					state = 'BY'
					print('leu caracter ( foi para BY')
				elif c.lower() == ')':
					state = 'BY'
					print('leu caracter ) foi para BY')
				elif c.lower() == '[':
					state = 'BY'
					print('leu caracter [ foi para BY')
				elif c.lower() == ']':
					state = 'BY'
					print('leu caracter ] foi para BY')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'BY'
					print('leu caracter \n foi para BY')
				elif c.lower() == '\t':
					state = 'BY'
					print('leu caracter \t foi para BY')
				elif c.lower() == ' ':
					state = 'BY'
					print('leu caracter   foi para BY')
				elif c.lower() == '0':
					state = 'BY'
					print('leu caracter 0 foi para BY')
				elif c.lower() == '1':
					state = 'BY'
					print('leu caracter 1 foi para BY')
				elif c.lower() == '2':
					state = 'BY'
					print('leu caracter 2 foi para BY')
				elif c.lower() == '3':
					state = 'BY'
					print('leu caracter 3 foi para BY')
				elif c.lower() == '4':
					state = 'BY'
					print('leu caracter 4 foi para BY')
				elif c.lower() == '5':
					state = 'BY'
					print('leu caracter 5 foi para BY')
				elif c.lower() == '6':
					state = 'BY'
					print('leu caracter 6 foi para BY')
				elif c.lower() == '7':
					state = 'BY'
					print('leu caracter 7 foi para BY')
				elif c.lower() == '8':
					state = 'BY'
					print('leu caracter 8 foi para BY')
				elif c.lower() == '9':
					state = 'BY'
					print('leu caracter 9 foi para BY')
				elif c.lower() == '\'':
					state = 'BY'
					print('leu caracter \' foi para BY')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BY':
				print('Tratar retorno estado final BY')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'BK':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'CA'
					print('leu caracter a foi para CA')
				elif c.lower() == 'b':
					state = 'CA'
					print('leu caracter b foi para CA')
				elif c.lower() == 'c':
					state = 'CA'
					print('leu caracter c foi para CA')
				elif c.lower() == 'd':
					state = 'CA'
					print('leu caracter d foi para CA')
				elif c.lower() == 'e':
					state = 'BZ'
					print('leu caracter e foi para BZ')
				elif c.lower() == 'f':
					state = 'CA'
					print('leu caracter f foi para CA')
				elif c.lower() == 'g':
					state = 'CA'
					print('leu caracter g foi para CA')
				elif c.lower() == 'h':
					state = 'CA'
					print('leu caracter h foi para CA')
				elif c.lower() == 'i':
					state = 'CA'
					print('leu caracter i foi para CA')
				elif c.lower() == 'j':
					state = 'CA'
					print('leu caracter j foi para CA')
				elif c.lower() == 'k':
					state = 'CA'
					print('leu caracter k foi para CA')
				elif c.lower() == 'l':
					state = 'CA'
					print('leu caracter l foi para CA')
				elif c.lower() == 'm':
					state = 'CA'
					print('leu caracter m foi para CA')
				elif c.lower() == 'n':
					state = 'CA'
					print('leu caracter n foi para CA')
				elif c.lower() == 'o':
					state = 'CA'
					print('leu caracter o foi para CA')
				elif c.lower() == 'p':
					state = 'CA'
					print('leu caracter p foi para CA')
				elif c.lower() == 'q':
					state = 'CA'
					print('leu caracter q foi para CA')
				elif c.lower() == 'r':
					state = 'CA'
					print('leu caracter r foi para CA')
				elif c.lower() == 's':
					state = 'CA'
					print('leu caracter s foi para CA')
				elif c.lower() == 't':
					state = 'CA'
					print('leu caracter t foi para CA')
				elif c.lower() == 'u':
					state = 'CA'
					print('leu caracter u foi para CA')
				elif c.lower() == 'v':
					state = 'CA'
					print('leu caracter v foi para CA')
				elif c.lower() == 'w':
					state = 'CA'
					print('leu caracter w foi para CA')
				elif c.lower() == 'x':
					state = 'CA'
					print('leu caracter x foi para CA')
				elif c.lower() == 'y':
					state = 'CA'
					print('leu caracter y foi para CA')
				elif c.lower() == 'z':
					state = 'CA'
					print('leu caracter z foi para CA')
				elif c.lower() == '_':
					state = 'CA'
					print('leu caracter _ foi para CA')
				elif c.lower() == '<':
					state = 'CA'
					print('leu caracter < foi para CA')
				elif c.lower() == '-':
					state = 'CA'
					print('leu caracter - foi para CA')
				elif c.lower() == '+':
					state = 'CA'
					print('leu caracter + foi para CA')
				elif c.lower() == '/':
					state = 'CA'
					print('leu caracter / foi para CA')
				elif c.lower() == '*':
					state = 'CA'
					print('leu caracter * foi para CA')
				elif c.lower() == '^':
					state = 'CA'
					print('leu caracter ^ foi para CA')
				elif c.lower() == '>':
					state = 'CA'
					print('leu caracter > foi para CA')
				elif c.lower() == '=':
					state = 'CA'
					print('leu caracter = foi para CA')
				elif c.lower() == '.':
					state = 'CA'
					print('leu caracter . foi para CA')
				elif c.lower() == ',':
					state = 'CA'
					print('leu caracter , foi para CA')
				elif c.lower() == ';':
					state = 'CA'
					print('leu caracter ; foi para CA')
				elif c.lower() == ':':
					state = 'CA'
					print('leu caracter : foi para CA')
				elif c.lower() == '(':
					state = 'CA'
					print('leu caracter ( foi para CA')
				elif c.lower() == ')':
					state = 'CA'
					print('leu caracter ) foi para CA')
				elif c.lower() == '[':
					state = 'CA'
					print('leu caracter [ foi para CA')
				elif c.lower() == ']':
					state = 'CA'
					print('leu caracter ] foi para CA')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'CA'
					print('leu caracter \n foi para CA')
				elif c.lower() == '\t':
					state = 'CA'
					print('leu caracter \t foi para CA')
				elif c.lower() == ' ':
					state = 'CA'
					print('leu caracter   foi para CA')
				elif c.lower() == '0':
					state = 'BK'
					print('leu caracter 0 foi para BK')
				elif c.lower() == '1':
					state = 'BK'
					print('leu caracter 1 foi para BK')
				elif c.lower() == '2':
					state = 'BK'
					print('leu caracter 2 foi para BK')
				elif c.lower() == '3':
					state = 'BK'
					print('leu caracter 3 foi para BK')
				elif c.lower() == '4':
					state = 'BK'
					print('leu caracter 4 foi para BK')
				elif c.lower() == '5':
					state = 'BK'
					print('leu caracter 5 foi para BK')
				elif c.lower() == '6':
					state = 'BK'
					print('leu caracter 6 foi para BK')
				elif c.lower() == '7':
					state = 'BK'
					print('leu caracter 7 foi para BK')
				elif c.lower() == '8':
					state = 'BK'
					print('leu caracter 8 foi para BK')
				elif c.lower() == '9':
					state = 'BK'
					print('leu caracter 9 foi para BK')
				elif c.lower() == '\'':
					state = 'CA'
					print('leu caracter \' foi para CA')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CA':
				print('Tratar retorno estado final CA')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'BM':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BN':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'CB'
					print('leu caracter < foi para CB')
				elif c.lower() == '-':
					state = 'CB'
					print('leu caracter - foi para CB')
				elif c.lower() == '+':
					state = 'CB'
					print('leu caracter + foi para CB')
				elif c.lower() == '/':
					state = 'CB'
					print('leu caracter / foi para CB')
				elif c.lower() == '*':
					state = 'CB'
					print('leu caracter * foi para CB')
				elif c.lower() == '^':
					state = 'CB'
					print('leu caracter ^ foi para CB')
				elif c.lower() == '>':
					state = 'CB'
					print('leu caracter > foi para CB')
				elif c.lower() == '=':
					state = 'CB'
					print('leu caracter = foi para CB')
				elif c.lower() == '.':
					state = 'CB'
					print('leu caracter . foi para CB')
				elif c.lower() == ',':
					state = 'CB'
					print('leu caracter , foi para CB')
				elif c.lower() == ';':
					state = 'CB'
					print('leu caracter ; foi para CB')
				elif c.lower() == ':':
					state = 'CB'
					print('leu caracter : foi para CB')
				elif c.lower() == '(':
					state = 'CB'
					print('leu caracter ( foi para CB')
				elif c.lower() == ')':
					state = 'CB'
					print('leu caracter ) foi para CB')
				elif c.lower() == '[':
					state = 'CB'
					print('leu caracter [ foi para CB')
				elif c.lower() == ']':
					state = 'CB'
					print('leu caracter ] foi para CB')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'CB'
					print('leu caracter \n foi para CB')
				elif c.lower() == '\t':
					state = 'CB'
					print('leu caracter \t foi para CB')
				elif c.lower() == ' ':
					state = 'CB'
					print('leu caracter   foi para CB')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'CB'
					print('leu caracter \' foi para CB')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CB':
				print('Tratar retorno estado final CB')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'BO':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BP':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'CD'
					print('leu caracter < foi para CD')
				elif c.lower() == '-':
					state = 'CD'
					print('leu caracter - foi para CD')
				elif c.lower() == '+':
					state = 'CD'
					print('leu caracter + foi para CD')
				elif c.lower() == '/':
					state = 'CD'
					print('leu caracter / foi para CD')
				elif c.lower() == '*':
					state = 'CD'
					print('leu caracter * foi para CD')
				elif c.lower() == '^':
					state = 'CD'
					print('leu caracter ^ foi para CD')
				elif c.lower() == '>':
					state = 'CD'
					print('leu caracter > foi para CD')
				elif c.lower() == '=':
					state = 'CD'
					print('leu caracter = foi para CD')
				elif c.lower() == '.':
					state = 'CD'
					print('leu caracter . foi para CD')
				elif c.lower() == ',':
					state = 'CD'
					print('leu caracter , foi para CD')
				elif c.lower() == ';':
					state = 'CD'
					print('leu caracter ; foi para CD')
				elif c.lower() == ':':
					state = 'CD'
					print('leu caracter : foi para CD')
				elif c.lower() == '(':
					state = 'CD'
					print('leu caracter ( foi para CD')
				elif c.lower() == ')':
					state = 'CD'
					print('leu caracter ) foi para CD')
				elif c.lower() == '[':
					state = 'CD'
					print('leu caracter [ foi para CD')
				elif c.lower() == ']':
					state = 'CD'
					print('leu caracter ] foi para CD')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'CD'
					print('leu caracter \n foi para CD')
				elif c.lower() == '\t':
					state = 'CD'
					print('leu caracter \t foi para CD')
				elif c.lower() == ' ':
					state = 'CD'
					print('leu caracter   foi para CD')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'CD'
					print('leu caracter \' foi para CD')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CD':
				print('Tratar retorno estado final CD')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'BQ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'CE'
					print('leu caracter < foi para CE')
				elif c.lower() == '-':
					state = 'CE'
					print('leu caracter - foi para CE')
				elif c.lower() == '+':
					state = 'CE'
					print('leu caracter + foi para CE')
				elif c.lower() == '/':
					state = 'CE'
					print('leu caracter / foi para CE')
				elif c.lower() == '*':
					state = 'CE'
					print('leu caracter * foi para CE')
				elif c.lower() == '^':
					state = 'CE'
					print('leu caracter ^ foi para CE')
				elif c.lower() == '>':
					state = 'CE'
					print('leu caracter > foi para CE')
				elif c.lower() == '=':
					state = 'CE'
					print('leu caracter = foi para CE')
				elif c.lower() == '.':
					state = 'CE'
					print('leu caracter . foi para CE')
				elif c.lower() == ',':
					state = 'CE'
					print('leu caracter , foi para CE')
				elif c.lower() == ';':
					state = 'CE'
					print('leu caracter ; foi para CE')
				elif c.lower() == ':':
					state = 'CE'
					print('leu caracter : foi para CE')
				elif c.lower() == '(':
					state = 'CE'
					print('leu caracter ( foi para CE')
				elif c.lower() == ')':
					state = 'CE'
					print('leu caracter ) foi para CE')
				elif c.lower() == '[':
					state = 'CE'
					print('leu caracter [ foi para CE')
				elif c.lower() == ']':
					state = 'CE'
					print('leu caracter ] foi para CE')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'CE'
					print('leu caracter \n foi para CE')
				elif c.lower() == '\t':
					state = 'CE'
					print('leu caracter \t foi para CE')
				elif c.lower() == ' ':
					state = 'CE'
					print('leu caracter   foi para CE')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'CE'
					print('leu caracter \' foi para CE')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CE':
				print('Tratar retorno estado final CE')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'BS':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'CF'
					print('leu caracter t foi para CF')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BT':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'CG'
					print('leu caracter i foi para CG')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BV':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'CH'
					print('leu caracter r foi para CH')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BW':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'CI'
					print('leu caracter t foi para CI')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BX':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'CJ'
					print('leu caracter o foi para CJ')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BZ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'ER'
					print('leu caracter a foi para ER')
				elif c.lower() == 'b':
					state = 'ER'
					print('leu caracter b foi para ER')
				elif c.lower() == 'c':
					state = 'ER'
					print('leu caracter c foi para ER')
				elif c.lower() == 'd':
					state = 'ER'
					print('leu caracter d foi para ER')
				elif c.lower() == 'e':
					state = 'ER'
					print('leu caracter e foi para ER')
				elif c.lower() == 'f':
					state = 'ER'
					print('leu caracter f foi para ER')
				elif c.lower() == 'g':
					state = 'ER'
					print('leu caracter g foi para ER')
				elif c.lower() == 'h':
					state = 'ER'
					print('leu caracter h foi para ER')
				elif c.lower() == 'i':
					state = 'ER'
					print('leu caracter i foi para ER')
				elif c.lower() == 'j':
					state = 'ER'
					print('leu caracter j foi para ER')
				elif c.lower() == 'k':
					state = 'ER'
					print('leu caracter k foi para ER')
				elif c.lower() == 'l':
					state = 'ER'
					print('leu caracter l foi para ER')
				elif c.lower() == 'm':
					state = 'ER'
					print('leu caracter m foi para ER')
				elif c.lower() == 'n':
					state = 'ER'
					print('leu caracter n foi para ER')
				elif c.lower() == 'o':
					state = 'ER'
					print('leu caracter o foi para ER')
				elif c.lower() == 'p':
					state = 'ER'
					print('leu caracter p foi para ER')
				elif c.lower() == 'q':
					state = 'ER'
					print('leu caracter q foi para ER')
				elif c.lower() == 'r':
					state = 'ER'
					print('leu caracter r foi para ER')
				elif c.lower() == 's':
					state = 'ER'
					print('leu caracter s foi para ER')
				elif c.lower() == 't':
					state = 'ER'
					print('leu caracter t foi para ER')
				elif c.lower() == 'u':
					state = 'ER'
					print('leu caracter u foi para ER')
				elif c.lower() == 'v':
					state = 'ER'
					print('leu caracter v foi para ER')
				elif c.lower() == 'w':
					state = 'ER'
					print('leu caracter w foi para ER')
				elif c.lower() == 'x':
					state = 'ER'
					print('leu caracter x foi para ER')
				elif c.lower() == 'y':
					state = 'ER'
					print('leu caracter y foi para ER')
				elif c.lower() == 'z':
					state = 'ER'
					print('leu caracter z foi para ER')
				elif c.lower() == '_':
					state = 'ER'
					print('leu caracter _ foi para ER')
				elif c.lower() == '<':
					state = 'ER'
					print('leu caracter < foi para ER')
				elif c.lower() == '-':
					state = 'CK'
					print('leu caracter - foi para CK')
				elif c.lower() == '+':
					state = 'CK'
					print('leu caracter + foi para CK')
				elif c.lower() == '/':
					state = 'ER'
					print('leu caracter / foi para ER')
				elif c.lower() == '*':
					state = 'ER'
					print('leu caracter * foi para ER')
				elif c.lower() == '^':
					state = 'ER'
					print('leu caracter ^ foi para ER')
				elif c.lower() == '>':
					state = 'ER'
					print('leu caracter > foi para ER')
				elif c.lower() == '=':
					state = 'ER'
					print('leu caracter = foi para ER')
				elif c.lower() == '.':
					state = 'ER'
					print('leu caracter . foi para ER')
				elif c.lower() == ',':
					state = 'ER'
					print('leu caracter , foi para ER')
				elif c.lower() == ';':
					state = 'ER'
					print('leu caracter ; foi para ER')
				elif c.lower() == ':':
					state = 'ER'
					print('leu caracter : foi para ER')
				elif c.lower() == '(':
					state = 'ER'
					print('leu caracter ( foi para ER')
				elif c.lower() == ')':
					state = 'ER'
					print('leu caracter ) foi para ER')
				elif c.lower() == '[':
					state = 'ER'
					print('leu caracter [ foi para ER')
				elif c.lower() == ']':
					state = 'ER'
					print('leu caracter ] foi para ER')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'ER'
					print('leu caracter \n foi para ER')
				elif c.lower() == '\t':
					state = 'ER'
					print('leu caracter \t foi para ER')
				elif c.lower() == ' ':
					state = 'ER'
					print('leu caracter   foi para ER')
				elif c.lower() == '0':
					state = 'CL'
					print('leu caracter 0 foi para CL')
				elif c.lower() == '1':
					state = 'CL'
					print('leu caracter 1 foi para CL')
				elif c.lower() == '2':
					state = 'CL'
					print('leu caracter 2 foi para CL')
				elif c.lower() == '3':
					state = 'CL'
					print('leu caracter 3 foi para CL')
				elif c.lower() == '4':
					state = 'CL'
					print('leu caracter 4 foi para CL')
				elif c.lower() == '5':
					state = 'CL'
					print('leu caracter 5 foi para CL')
				elif c.lower() == '6':
					state = 'CL'
					print('leu caracter 6 foi para CL')
				elif c.lower() == '7':
					state = 'CL'
					print('leu caracter 7 foi para CL')
				elif c.lower() == '8':
					state = 'CL'
					print('leu caracter 8 foi para CL')
				elif c.lower() == '9':
					state = 'CL'
					print('leu caracter 9 foi para CL')
				elif c.lower() == '\'':
					state = 'ER'
					print('leu caracter \' foi para ER')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CC':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'CM'
					print('leu caracter n foi para CM')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CF':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'CN'
					print('leu caracter < foi para CN')
				elif c.lower() == '-':
					state = 'CN'
					print('leu caracter - foi para CN')
				elif c.lower() == '+':
					state = 'CN'
					print('leu caracter + foi para CN')
				elif c.lower() == '/':
					state = 'CN'
					print('leu caracter / foi para CN')
				elif c.lower() == '*':
					state = 'CN'
					print('leu caracter * foi para CN')
				elif c.lower() == '^':
					state = 'CN'
					print('leu caracter ^ foi para CN')
				elif c.lower() == '>':
					state = 'CN'
					print('leu caracter > foi para CN')
				elif c.lower() == '=':
					state = 'CN'
					print('leu caracter = foi para CN')
				elif c.lower() == '.':
					state = 'CN'
					print('leu caracter . foi para CN')
				elif c.lower() == ',':
					state = 'CN'
					print('leu caracter , foi para CN')
				elif c.lower() == ';':
					state = 'CN'
					print('leu caracter ; foi para CN')
				elif c.lower() == ':':
					state = 'CN'
					print('leu caracter : foi para CN')
				elif c.lower() == '(':
					state = 'CN'
					print('leu caracter ( foi para CN')
				elif c.lower() == ')':
					state = 'CN'
					print('leu caracter ) foi para CN')
				elif c.lower() == '[':
					state = 'CN'
					print('leu caracter [ foi para CN')
				elif c.lower() == ']':
					state = 'CN'
					print('leu caracter ] foi para CN')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'CN'
					print('leu caracter \n foi para CN')
				elif c.lower() == '\t':
					state = 'CN'
					print('leu caracter \t foi para CN')
				elif c.lower() == ' ':
					state = 'CN'
					print('leu caracter   foi para CN')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'CN'
					print('leu caracter \' foi para CN')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CN':
				print('Tratar retorno estado final CN')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'CG':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'CO'
					print('leu caracter o foi para CO')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CH':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'CP'
					print('leu caracter a foi para CP')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CI':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'CQ'
					print('leu caracter a foi para CQ')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CJ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'CR'
					print('leu caracter < foi para CR')
				elif c.lower() == '-':
					state = 'CR'
					print('leu caracter - foi para CR')
				elif c.lower() == '+':
					state = 'CR'
					print('leu caracter + foi para CR')
				elif c.lower() == '/':
					state = 'CR'
					print('leu caracter / foi para CR')
				elif c.lower() == '*':
					state = 'CR'
					print('leu caracter * foi para CR')
				elif c.lower() == '^':
					state = 'CR'
					print('leu caracter ^ foi para CR')
				elif c.lower() == '>':
					state = 'CR'
					print('leu caracter > foi para CR')
				elif c.lower() == '=':
					state = 'CR'
					print('leu caracter = foi para CR')
				elif c.lower() == '.':
					state = 'CR'
					print('leu caracter . foi para CR')
				elif c.lower() == ',':
					state = 'CR'
					print('leu caracter , foi para CR')
				elif c.lower() == ';':
					state = 'CR'
					print('leu caracter ; foi para CR')
				elif c.lower() == ':':
					state = 'CR'
					print('leu caracter : foi para CR')
				elif c.lower() == '(':
					state = 'CR'
					print('leu caracter ( foi para CR')
				elif c.lower() == ')':
					state = 'CR'
					print('leu caracter ) foi para CR')
				elif c.lower() == '[':
					state = 'CR'
					print('leu caracter [ foi para CR')
				elif c.lower() == ']':
					state = 'CR'
					print('leu caracter ] foi para CR')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'CR'
					print('leu caracter \n foi para CR')
				elif c.lower() == '\t':
					state = 'CR'
					print('leu caracter \t foi para CR')
				elif c.lower() == ' ':
					state = 'CR'
					print('leu caracter   foi para CR')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'CR'
					print('leu caracter \' foi para CR')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CR':
				print('Tratar retorno estado final CR')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'CK':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'ER'
					print('leu caracter a foi para ER')
				elif c.lower() == 'b':
					state = 'ER'
					print('leu caracter b foi para ER')
				elif c.lower() == 'c':
					state = 'ER'
					print('leu caracter c foi para ER')
				elif c.lower() == 'd':
					state = 'ER'
					print('leu caracter d foi para ER')
				elif c.lower() == 'e':
					state = 'ER'
					print('leu caracter e foi para ER')
				elif c.lower() == 'f':
					state = 'ER'
					print('leu caracter f foi para ER')
				elif c.lower() == 'g':
					state = 'ER'
					print('leu caracter g foi para ER')
				elif c.lower() == 'h':
					state = 'ER'
					print('leu caracter h foi para ER')
				elif c.lower() == 'i':
					state = 'ER'
					print('leu caracter i foi para ER')
				elif c.lower() == 'j':
					state = 'ER'
					print('leu caracter j foi para ER')
				elif c.lower() == 'k':
					state = 'ER'
					print('leu caracter k foi para ER')
				elif c.lower() == 'l':
					state = 'ER'
					print('leu caracter l foi para ER')
				elif c.lower() == 'm':
					state = 'ER'
					print('leu caracter m foi para ER')
				elif c.lower() == 'n':
					state = 'ER'
					print('leu caracter n foi para ER')
				elif c.lower() == 'o':
					state = 'ER'
					print('leu caracter o foi para ER')
				elif c.lower() == 'p':
					state = 'ER'
					print('leu caracter p foi para ER')
				elif c.lower() == 'q':
					state = 'ER'
					print('leu caracter q foi para ER')
				elif c.lower() == 'r':
					state = 'ER'
					print('leu caracter r foi para ER')
				elif c.lower() == 's':
					state = 'ER'
					print('leu caracter s foi para ER')
				elif c.lower() == 't':
					state = 'ER'
					print('leu caracter t foi para ER')
				elif c.lower() == 'u':
					state = 'ER'
					print('leu caracter u foi para ER')
				elif c.lower() == 'v':
					state = 'ER'
					print('leu caracter v foi para ER')
				elif c.lower() == 'w':
					state = 'ER'
					print('leu caracter w foi para ER')
				elif c.lower() == 'x':
					state = 'ER'
					print('leu caracter x foi para ER')
				elif c.lower() == 'y':
					state = 'ER'
					print('leu caracter y foi para ER')
				elif c.lower() == 'z':
					state = 'ER'
					print('leu caracter z foi para ER')
				elif c.lower() == '_':
					state = 'ER'
					print('leu caracter _ foi para ER')
				elif c.lower() == '<':
					state = 'ER'
					print('leu caracter < foi para ER')
				elif c.lower() == '-':
					state = 'ER'
					print('leu caracter - foi para ER')
				elif c.lower() == '+':
					state = 'ER'
					print('leu caracter + foi para ER')
				elif c.lower() == '/':
					state = 'ER'
					print('leu caracter / foi para ER')
				elif c.lower() == '*':
					state = 'ER'
					print('leu caracter * foi para ER')
				elif c.lower() == '^':
					state = 'ER'
					print('leu caracter ^ foi para ER')
				elif c.lower() == '>':
					state = 'ER'
					print('leu caracter > foi para ER')
				elif c.lower() == '=':
					state = 'ER'
					print('leu caracter = foi para ER')
				elif c.lower() == '.':
					state = 'ER'
					print('leu caracter . foi para ER')
				elif c.lower() == ',':
					state = 'ER'
					print('leu caracter , foi para ER')
				elif c.lower() == ';':
					state = 'ER'
					print('leu caracter ; foi para ER')
				elif c.lower() == ':':
					state = 'ER'
					print('leu caracter : foi para ER')
				elif c.lower() == '(':
					state = 'ER'
					print('leu caracter ( foi para ER')
				elif c.lower() == ')':
					state = 'ER'
					print('leu caracter ) foi para ER')
				elif c.lower() == '[':
					state = 'ER'
					print('leu caracter [ foi para ER')
				elif c.lower() == ']':
					state = 'ER'
					print('leu caracter ] foi para ER')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'ER'
					print('leu caracter \n foi para ER')
				elif c.lower() == '\t':
					state = 'ER'
					print('leu caracter \t foi para ER')
				elif c.lower() == ' ':
					state = 'ER'
					print('leu caracter   foi para ER')
				elif c.lower() == '0':
					state = 'CL'
					print('leu caracter 0 foi para CL')
				elif c.lower() == '1':
					state = 'CL'
					print('leu caracter 1 foi para CL')
				elif c.lower() == '2':
					state = 'CL'
					print('leu caracter 2 foi para CL')
				elif c.lower() == '3':
					state = 'CL'
					print('leu caracter 3 foi para CL')
				elif c.lower() == '4':
					state = 'CL'
					print('leu caracter 4 foi para CL')
				elif c.lower() == '5':
					state = 'CL'
					print('leu caracter 5 foi para CL')
				elif c.lower() == '6':
					state = 'CL'
					print('leu caracter 6 foi para CL')
				elif c.lower() == '7':
					state = 'CL'
					print('leu caracter 7 foi para CL')
				elif c.lower() == '8':
					state = 'CL'
					print('leu caracter 8 foi para CL')
				elif c.lower() == '9':
					state = 'CL'
					print('leu caracter 9 foi para CL')
				elif c.lower() == '\'':
					state = 'ER'
					print('leu caracter \' foi para ER')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CL':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'CS'
					print('leu caracter a foi para CS')
				elif c.lower() == 'b':
					state = 'CS'
					print('leu caracter b foi para CS')
				elif c.lower() == 'c':
					state = 'CS'
					print('leu caracter c foi para CS')
				elif c.lower() == 'd':
					state = 'CS'
					print('leu caracter d foi para CS')
				elif c.lower() == 'e':
					state = 'CS'
					print('leu caracter e foi para CS')
				elif c.lower() == 'f':
					state = 'CS'
					print('leu caracter f foi para CS')
				elif c.lower() == 'g':
					state = 'CS'
					print('leu caracter g foi para CS')
				elif c.lower() == 'h':
					state = 'CS'
					print('leu caracter h foi para CS')
				elif c.lower() == 'i':
					state = 'CS'
					print('leu caracter i foi para CS')
				elif c.lower() == 'j':
					state = 'CS'
					print('leu caracter j foi para CS')
				elif c.lower() == 'k':
					state = 'CS'
					print('leu caracter k foi para CS')
				elif c.lower() == 'l':
					state = 'CS'
					print('leu caracter l foi para CS')
				elif c.lower() == 'm':
					state = 'CS'
					print('leu caracter m foi para CS')
				elif c.lower() == 'n':
					state = 'CS'
					print('leu caracter n foi para CS')
				elif c.lower() == 'o':
					state = 'CS'
					print('leu caracter o foi para CS')
				elif c.lower() == 'p':
					state = 'CS'
					print('leu caracter p foi para CS')
				elif c.lower() == 'q':
					state = 'CS'
					print('leu caracter q foi para CS')
				elif c.lower() == 'r':
					state = 'CS'
					print('leu caracter r foi para CS')
				elif c.lower() == 's':
					state = 'CS'
					print('leu caracter s foi para CS')
				elif c.lower() == 't':
					state = 'CS'
					print('leu caracter t foi para CS')
				elif c.lower() == 'u':
					state = 'CS'
					print('leu caracter u foi para CS')
				elif c.lower() == 'v':
					state = 'CS'
					print('leu caracter v foi para CS')
				elif c.lower() == 'w':
					state = 'CS'
					print('leu caracter w foi para CS')
				elif c.lower() == 'x':
					state = 'CS'
					print('leu caracter x foi para CS')
				elif c.lower() == 'y':
					state = 'CS'
					print('leu caracter y foi para CS')
				elif c.lower() == 'z':
					state = 'CS'
					print('leu caracter z foi para CS')
				elif c.lower() == '_':
					state = 'CS'
					print('leu caracter _ foi para CS')
				elif c.lower() == '<':
					state = 'CS'
					print('leu caracter < foi para CS')
				elif c.lower() == '-':
					state = 'CS'
					print('leu caracter - foi para CS')
				elif c.lower() == '+':
					state = 'CS'
					print('leu caracter + foi para CS')
				elif c.lower() == '/':
					state = 'CS'
					print('leu caracter / foi para CS')
				elif c.lower() == '*':
					state = 'CS'
					print('leu caracter * foi para CS')
				elif c.lower() == '^':
					state = 'CS'
					print('leu caracter ^ foi para CS')
				elif c.lower() == '>':
					state = 'CS'
					print('leu caracter > foi para CS')
				elif c.lower() == '=':
					state = 'CS'
					print('leu caracter = foi para CS')
				elif c.lower() == '.':
					state = 'CS'
					print('leu caracter . foi para CS')
				elif c.lower() == ',':
					state = 'CS'
					print('leu caracter , foi para CS')
				elif c.lower() == ';':
					state = 'CS'
					print('leu caracter ; foi para CS')
				elif c.lower() == ':':
					state = 'CS'
					print('leu caracter : foi para CS')
				elif c.lower() == '(':
					state = 'CS'
					print('leu caracter ( foi para CS')
				elif c.lower() == ')':
					state = 'CS'
					print('leu caracter ) foi para CS')
				elif c.lower() == '[':
					state = 'CS'
					print('leu caracter [ foi para CS')
				elif c.lower() == ']':
					state = 'CS'
					print('leu caracter ] foi para CS')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'CS'
					print('leu caracter \n foi para CS')
				elif c.lower() == '\t':
					state = 'CS'
					print('leu caracter \t foi para CS')
				elif c.lower() == ' ':
					state = 'CS'
					print('leu caracter   foi para CS')
				elif c.lower() == '0':
					state = 'CL'
					print('leu caracter 0 foi para CL')
				elif c.lower() == '1':
					state = 'CL'
					print('leu caracter 1 foi para CL')
				elif c.lower() == '2':
					state = 'CL'
					print('leu caracter 2 foi para CL')
				elif c.lower() == '3':
					state = 'CL'
					print('leu caracter 3 foi para CL')
				elif c.lower() == '4':
					state = 'CL'
					print('leu caracter 4 foi para CL')
				elif c.lower() == '5':
					state = 'CL'
					print('leu caracter 5 foi para CL')
				elif c.lower() == '6':
					state = 'CL'
					print('leu caracter 6 foi para CL')
				elif c.lower() == '7':
					state = 'CL'
					print('leu caracter 7 foi para CL')
				elif c.lower() == '8':
					state = 'CL'
					print('leu caracter 8 foi para CL')
				elif c.lower() == '9':
					state = 'CL'
					print('leu caracter 9 foi para CL')
				elif c.lower() == '\'':
					state = 'CS'
					print('leu caracter \' foi para CS')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CS':
				print('Tratar retorno estado final CS')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'CM':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'CV'
					print('leu caracter m foi para CV')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'CT'
					print('leu caracter t foi para CT')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CO':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'CU'
					print('leu caracter < foi para CU')
				elif c.lower() == '-':
					state = 'CU'
					print('leu caracter - foi para CU')
				elif c.lower() == '+':
					state = 'CU'
					print('leu caracter + foi para CU')
				elif c.lower() == '/':
					state = 'CU'
					print('leu caracter / foi para CU')
				elif c.lower() == '*':
					state = 'CU'
					print('leu caracter * foi para CU')
				elif c.lower() == '^':
					state = 'CU'
					print('leu caracter ^ foi para CU')
				elif c.lower() == '>':
					state = 'CU'
					print('leu caracter > foi para CU')
				elif c.lower() == '=':
					state = 'CU'
					print('leu caracter = foi para CU')
				elif c.lower() == '.':
					state = 'CU'
					print('leu caracter . foi para CU')
				elif c.lower() == ',':
					state = 'CU'
					print('leu caracter , foi para CU')
				elif c.lower() == ';':
					state = 'CU'
					print('leu caracter ; foi para CU')
				elif c.lower() == ':':
					state = 'CU'
					print('leu caracter : foi para CU')
				elif c.lower() == '(':
					state = 'CU'
					print('leu caracter ( foi para CU')
				elif c.lower() == ')':
					state = 'CU'
					print('leu caracter ) foi para CU')
				elif c.lower() == '[':
					state = 'CU'
					print('leu caracter [ foi para CU')
				elif c.lower() == ']':
					state = 'CU'
					print('leu caracter ] foi para CU')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'CU'
					print('leu caracter \n foi para CU')
				elif c.lower() == '\t':
					state = 'CU'
					print('leu caracter \t foi para CU')
				elif c.lower() == ' ':
					state = 'CU'
					print('leu caracter   foi para CU')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'CU'
					print('leu caracter \' foi para CU')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CU':
				print('Tratar retorno estado final CU')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'CP':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'CV'
					print('leu caracter m foi para CV')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CQ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'CW'
					print('leu caracter < foi para CW')
				elif c.lower() == '-':
					state = 'CW'
					print('leu caracter - foi para CW')
				elif c.lower() == '+':
					state = 'CW'
					print('leu caracter + foi para CW')
				elif c.lower() == '/':
					state = 'CW'
					print('leu caracter / foi para CW')
				elif c.lower() == '*':
					state = 'CW'
					print('leu caracter * foi para CW')
				elif c.lower() == '^':
					state = 'CW'
					print('leu caracter ^ foi para CW')
				elif c.lower() == '>':
					state = 'CW'
					print('leu caracter > foi para CW')
				elif c.lower() == '=':
					state = 'CW'
					print('leu caracter = foi para CW')
				elif c.lower() == '.':
					state = 'CW'
					print('leu caracter . foi para CW')
				elif c.lower() == ',':
					state = 'CW'
					print('leu caracter , foi para CW')
				elif c.lower() == ';':
					state = 'CW'
					print('leu caracter ; foi para CW')
				elif c.lower() == ':':
					state = 'CW'
					print('leu caracter : foi para CW')
				elif c.lower() == '(':
					state = 'CW'
					print('leu caracter ( foi para CW')
				elif c.lower() == ')':
					state = 'CW'
					print('leu caracter ) foi para CW')
				elif c.lower() == '[':
					state = 'CW'
					print('leu caracter [ foi para CW')
				elif c.lower() == ']':
					state = 'CW'
					print('leu caracter ] foi para CW')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'CW'
					print('leu caracter \n foi para CW')
				elif c.lower() == '\t':
					state = 'CW'
					print('leu caracter \t foi para CW')
				elif c.lower() == ' ':
					state = 'CW'
					print('leu caracter   foi para CW')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'CW'
					print('leu caracter \' foi para CW')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CW':
				print('Tratar retorno estado final CW')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'CT':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'CX'
					print('leu caracter o foi para CX')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CV':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'CY'
					print('leu caracter a foi para CY')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'AC'
					print('leu caracter < foi para AC')
				elif c.lower() == '-':
					state = 'AC'
					print('leu caracter - foi para AC')
				elif c.lower() == '+':
					state = 'AC'
					print('leu caracter + foi para AC')
				elif c.lower() == '/':
					state = 'AC'
					print('leu caracter / foi para AC')
				elif c.lower() == '*':
					state = 'AC'
					print('leu caracter * foi para AC')
				elif c.lower() == '^':
					state = 'AC'
					print('leu caracter ^ foi para AC')
				elif c.lower() == '>':
					state = 'AC'
					print('leu caracter > foi para AC')
				elif c.lower() == '=':
					state = 'AC'
					print('leu caracter = foi para AC')
				elif c.lower() == '.':
					state = 'AC'
					print('leu caracter . foi para AC')
				elif c.lower() == ',':
					state = 'AC'
					print('leu caracter , foi para AC')
				elif c.lower() == ';':
					state = 'AC'
					print('leu caracter ; foi para AC')
				elif c.lower() == ':':
					state = 'AC'
					print('leu caracter : foi para AC')
				elif c.lower() == '(':
					state = 'AC'
					print('leu caracter ( foi para AC')
				elif c.lower() == ')':
					state = 'AC'
					print('leu caracter ) foi para AC')
				elif c.lower() == '[':
					state = 'AC'
					print('leu caracter [ foi para AC')
				elif c.lower() == ']':
					state = 'AC'
					print('leu caracter ] foi para AC')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'AC'
					print('leu caracter \n foi para AC')
				elif c.lower() == '\t':
					state = 'AC'
					print('leu caracter \t foi para AC')
				elif c.lower() == ' ':
					state = 'AC'
					print('leu caracter   foi para AC')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'AC'
					print('leu caracter \' foi para AC')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CX':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'CZ'
					print('leu caracter < foi para CZ')
				elif c.lower() == '-':
					state = 'CZ'
					print('leu caracter - foi para CZ')
				elif c.lower() == '+':
					state = 'CZ'
					print('leu caracter + foi para CZ')
				elif c.lower() == '/':
					state = 'CZ'
					print('leu caracter / foi para CZ')
				elif c.lower() == '*':
					state = 'CZ'
					print('leu caracter * foi para CZ')
				elif c.lower() == '^':
					state = 'CZ'
					print('leu caracter ^ foi para CZ')
				elif c.lower() == '>':
					state = 'CZ'
					print('leu caracter > foi para CZ')
				elif c.lower() == '=':
					state = 'CZ'
					print('leu caracter = foi para CZ')
				elif c.lower() == '.':
					state = 'CZ'
					print('leu caracter . foi para CZ')
				elif c.lower() == ',':
					state = 'CZ'
					print('leu caracter , foi para CZ')
				elif c.lower() == ';':
					state = 'CZ'
					print('leu caracter ; foi para CZ')
				elif c.lower() == ':':
					state = 'CZ'
					print('leu caracter : foi para CZ')
				elif c.lower() == '(':
					state = 'CZ'
					print('leu caracter ( foi para CZ')
				elif c.lower() == ')':
					state = 'CZ'
					print('leu caracter ) foi para CZ')
				elif c.lower() == '[':
					state = 'CZ'
					print('leu caracter [ foi para CZ')
				elif c.lower() == ']':
					state = 'CZ'
					print('leu caracter ] foi para CZ')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'CZ'
					print('leu caracter \n foi para CZ')
				elif c.lower() == '\t':
					state = 'CZ'
					print('leu caracter \t foi para CZ')
				elif c.lower() == ' ':
					state = 'CZ'
					print('leu caracter   foi para CZ')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'CZ'
					print('leu caracter \' foi para CZ')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CZ':
				print('Tratar retorno estado final CZ')
				print(f"Identificador montado {id}")
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'CY':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print('leu caracter a foi para C')
				elif c.lower() == 'b':
					state = 'C'
					print('leu caracter b foi para C')
				elif c.lower() == 'c':
					state = 'C'
					print('leu caracter c foi para C')
				elif c.lower() == 'd':
					state = 'C'
					print('leu caracter d foi para C')
				elif c.lower() == 'e':
					state = 'C'
					print('leu caracter e foi para C')
				elif c.lower() == 'f':
					state = 'C'
					print('leu caracter f foi para C')
				elif c.lower() == 'g':
					state = 'C'
					print('leu caracter g foi para C')
				elif c.lower() == 'h':
					state = 'C'
					print('leu caracter h foi para C')
				elif c.lower() == 'i':
					state = 'C'
					print('leu caracter i foi para C')
				elif c.lower() == 'j':
					state = 'C'
					print('leu caracter j foi para C')
				elif c.lower() == 'k':
					state = 'C'
					print('leu caracter k foi para C')
				elif c.lower() == 'l':
					state = 'C'
					print('leu caracter l foi para C')
				elif c.lower() == 'm':
					state = 'C'
					print('leu caracter m foi para C')
				elif c.lower() == 'n':
					state = 'C'
					print('leu caracter n foi para C')
				elif c.lower() == 'o':
					state = 'C'
					print('leu caracter o foi para C')
				elif c.lower() == 'p':
					state = 'C'
					print('leu caracter p foi para C')
				elif c.lower() == 'q':
					state = 'C'
					print('leu caracter q foi para C')
				elif c.lower() == 'r':
					state = 'C'
					print('leu caracter r foi para C')
				elif c.lower() == 's':
					state = 'C'
					print('leu caracter s foi para C')
				elif c.lower() == 't':
					state = 'C'
					print('leu caracter t foi para C')
				elif c.lower() == 'u':
					state = 'C'
					print('leu caracter u foi para C')
				elif c.lower() == 'v':
					state = 'C'
					print('leu caracter v foi para C')
				elif c.lower() == 'w':
					state = 'C'
					print('leu caracter w foi para C')
				elif c.lower() == 'x':
					state = 'C'
					print('leu caracter x foi para C')
				elif c.lower() == 'y':
					state = 'C'
					print('leu caracter y foi para C')
				elif c.lower() == 'z':
					state = 'C'
					print('leu caracter z foi para C')
				elif c.lower() == '_':
					state = 'C'
					print('leu caracter _ foi para C')
				elif c.lower() == '<':
					state = 'DA'
					print('leu caracter < foi para DA')
				elif c.lower() == '-':
					state = 'DA'
					print('leu caracter - foi para DA')
				elif c.lower() == '+':
					state = 'DA'
					print('leu caracter + foi para DA')
				elif c.lower() == '/':
					state = 'DA'
					print('leu caracter / foi para DA')
				elif c.lower() == '*':
					state = 'DA'
					print('leu caracter * foi para DA')
				elif c.lower() == '^':
					state = 'DA'
					print('leu caracter ^ foi para DA')
				elif c.lower() == '>':
					state = 'DA'
					print('leu caracter > foi para DA')
				elif c.lower() == '=':
					state = 'DA'
					print('leu caracter = foi para DA')
				elif c.lower() == '.':
					state = 'DA'
					print('leu caracter . foi para DA')
				elif c.lower() == ',':
					state = 'DA'
					print('leu caracter , foi para DA')
				elif c.lower() == ';':
					state = 'DA'
					print('leu caracter ; foi para DA')
				elif c.lower() == ':':
					state = 'DA'
					print('leu caracter : foi para DA')
				elif c.lower() == '(':
					state = 'DA'
					print('leu caracter ( foi para DA')
				elif c.lower() == ')':
					state = 'DA'
					print('leu caracter ) foi para DA')
				elif c.lower() == '[':
					state = 'DA'
					print('leu caracter [ foi para DA')
				elif c.lower() == ']':
					state = 'DA'
					print('leu caracter ] foi para DA')
				elif c.lower() == '\n':
					linhaGlobal += 1
					state = 'DA'
					print('leu caracter \n foi para DA')
				elif c.lower() == '\t':
					state = 'DA'
					print('leu caracter \t foi para DA')
				elif c.lower() == ' ':
					state = 'DA'
					print('leu caracter   foi para DA')
				elif c.lower() == '0':
					state = 'C'
					print('leu caracter 0 foi para C')
				elif c.lower() == '1':
					state = 'C'
					print('leu caracter 1 foi para C')
				elif c.lower() == '2':
					state = 'C'
					print('leu caracter 2 foi para C')
				elif c.lower() == '3':
					state = 'C'
					print('leu caracter 3 foi para C')
				elif c.lower() == '4':
					state = 'C'
					print('leu caracter 4 foi para C')
				elif c.lower() == '5':
					state = 'C'
					print('leu caracter 5 foi para C')
				elif c.lower() == '6':
					state = 'C'
					print('leu caracter 6 foi para C')
				elif c.lower() == '7':
					state = 'C'
					print('leu caracter 7 foi para C')
				elif c.lower() == '8':
					state = 'C'
					print('leu caracter 8 foi para C')
				elif c.lower() == '9':
					state = 'C'
					print('leu caracter 9 foi para C')
				elif c.lower() == '\'':
					state = 'DA'
					print('leu caracter \' foi para DA')
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'W':
				c = nextChar()
				if c == ']':
					state = 'X'
				else:
					state = 'W'
			case 'DA':
				print('Tratar retorno estado final DA')
				state = 'A'
				lerProx = False
				if c not in ['\n', '\t', ' ']:
					f.seek(f.tell()-1)
				return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)

while True:
	try:
		token = cod_direta()
		print(f"<{token.tipo}, {token.atributo}, {token.linha}, {token.coluna}>")
		if token.tipo == 'Erro':
			break
	except EOFError:
		break
