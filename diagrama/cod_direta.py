linhaGlobal = 0
colunaGlobal = 0
tabelaSimbolos = {}
def lex():
	state = 'A'
	c = ''
	id = ''
	global linhaGlobal
	global colunaGlobal
	global tabelaSimbolos
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
					print(f"leu caracter a foi para B linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'D'
					print(f"leu caracter c foi para D linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'E'
					print(f"leu caracter e foi para E linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'F'
					print(f"leu caracter f foi para F linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'G'
					print(f"leu caracter i foi para G linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'H'
					print(f"leu caracter p foi para H linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'I'
					print(f"leu caracter r foi para I linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'J'
					print(f"leu caracter s foi para J linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'K'
					print(f"leu caracter < foi para K linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'L'
					print(f"leu caracter - foi para L linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'M'
					print(f"leu caracter + foi para M linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'N'
					print(f"leu caracter / foi para N linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'O'
					print(f"leu caracter * foi para O linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'P'
					print(f"leu caracter ^ foi para P linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'Q'
					print(f"leu caracter > foi para Q linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'R'
					print(f"leu caracter = foi para R linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'ER'
					print(f"leu caracter . foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'S'
					print(f"leu caracter , foi para S linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'T'
					print(f"leu caracter ; foi para T linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'RA'
					print(f"leu caracter : foi para RA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'U'
					print(f"leu caracter ( foi para U linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'V'
					print(f"leu caracter ) foi para V linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'W'
					print(f"leu caracter [ foi para W linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'X'
					print(f"leu caracter ] foi para X linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'Y'
					print(f"leu caracter \n foi para Y linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'Y'
					print(f"leu caracter \t foi para Y linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'Y'
					print(f"leu caracter   foi para Y linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'Z'
					print(f"leu caracter 0 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'Z'
					print(f"leu caracter 1 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'Z'
					print(f"leu caracter 2 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'Z'
					print(f"leu caracter 3 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'Z'
					print(f"leu caracter 4 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'Z'
					print(f"leu caracter 5 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'Z'
					print(f"leu caracter 6 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'Z'
					print(f"leu caracter 7 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'Z'
					print(f"leu caracter 8 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'Z'
					print(f"leu caracter 9 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AA'
					print(f"leu caracter \' foi para AA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'ER':
				print('Tratar retorno estado final ER')
				print(f"Identificador montado {id}")
				state = 'A'
				return Token('Erro','ATRIBUTO',linhaGlobal,colunaGlobal)
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
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
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'AB'
					print(f"leu caracter t foi para AB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'C':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'D':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'AD'
					print(f"leu caracter h foi para AD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'E':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'AE'
					print(f"leu caracter n foi para AE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'F':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AF'
					print(f"leu caracter a foi para AF linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'AG'
					print(f"leu caracter i foi para AG linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'AH'
					print(f"leu caracter l foi para AH linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'G':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'AI'
					print(f"leu caracter n foi para AI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'H':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'AJ'
					print(f"leu caracter r foi para AJ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'I':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'AK'
					print(f"leu caracter e foi para AK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'J':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'AL'
					print(f"leu caracter e foi para AL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'K':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AM'
					print(f"leu caracter a foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'AM'
					print(f"leu caracter b foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'AM'
					print(f"leu caracter c foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'AM'
					print(f"leu caracter d foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'AM'
					print(f"leu caracter e foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'AM'
					print(f"leu caracter f foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'AM'
					print(f"leu caracter g foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'AM'
					print(f"leu caracter h foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'AM'
					print(f"leu caracter i foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'AM'
					print(f"leu caracter j foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'AM'
					print(f"leu caracter k foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'AM'
					print(f"leu caracter l foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'AM'
					print(f"leu caracter m foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'AM'
					print(f"leu caracter n foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'AM'
					print(f"leu caracter o foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'AM'
					print(f"leu caracter p foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'AM'
					print(f"leu caracter q foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'AM'
					print(f"leu caracter r foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'AM'
					print(f"leu caracter s foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'AM'
					print(f"leu caracter t foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'AM'
					print(f"leu caracter u foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'AM'
					print(f"leu caracter v foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'AM'
					print(f"leu caracter w foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'AM'
					print(f"leu caracter x foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'AM'
					print(f"leu caracter y foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'AM'
					print(f"leu caracter z foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'AM'
					print(f"leu caracter _ foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AM'
					print(f"leu caracter < foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AN'
					print(f"leu caracter - foi para AN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AM'
					print(f"leu caracter + foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AM'
					print(f"leu caracter / foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AM'
					print(f"leu caracter * foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AM'
					print(f"leu caracter ^ foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AO'
					print(f"leu caracter > foi para AO linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AP'
					print(f"leu caracter = foi para AP linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AM'
					print(f"leu caracter . foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AM'
					print(f"leu caracter , foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AM'
					print(f"leu caracter ; foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AM'
					print(f"leu caracter : foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AM'
					print(f"leu caracter ( foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AM'
					print(f"leu caracter ) foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AM'
					print(f"leu caracter [ foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AM'
					print(f"leu caracter ] foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AM'
					print(f"leu caracter \n foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AM'
					print(f"leu caracter \t foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AM'
					print(f"leu caracter   foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'AM'
					print(f"leu caracter 0 foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'AM'
					print(f"leu caracter 1 foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'AM'
					print(f"leu caracter 2 foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'AM'
					print(f"leu caracter 3 foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'AM'
					print(f"leu caracter 4 foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'AM'
					print(f"leu caracter 5 foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'AM'
					print(f"leu caracter 6 foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'AM'
					print(f"leu caracter 7 foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'AM'
					print(f"leu caracter 8 foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'AM'
					print(f"leu caracter 9 foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AM'
					print(f"leu caracter \' foi para AM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AO':
				print('Tratar retorno estado final AO')
				print(f"Identificador montado {id}")
				state = 'A'
				print(id)
				print(c)
				tabelaSimbolos[id.strip()] = Atributo('',id.strip())
				return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AP':
				print('Tratar retorno estado final AP')
				print(f"Identificador montado {id}")
				state = 'A'
				print(id)
				print(c)
				tabelaSimbolos[id.strip()] = Atributo('',id.strip())
				return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'Q':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AQ'
					print(f"leu caracter a foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'AQ'
					print(f"leu caracter b foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'AQ'
					print(f"leu caracter c foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'AQ'
					print(f"leu caracter d foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'AQ'
					print(f"leu caracter e foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'AQ'
					print(f"leu caracter f foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'AQ'
					print(f"leu caracter g foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'AQ'
					print(f"leu caracter h foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'AQ'
					print(f"leu caracter i foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'AQ'
					print(f"leu caracter j foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'AQ'
					print(f"leu caracter k foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'AQ'
					print(f"leu caracter l foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'AQ'
					print(f"leu caracter m foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'AQ'
					print(f"leu caracter n foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'AQ'
					print(f"leu caracter o foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'AQ'
					print(f"leu caracter p foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'AQ'
					print(f"leu caracter q foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'AQ'
					print(f"leu caracter r foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'AQ'
					print(f"leu caracter s foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'AQ'
					print(f"leu caracter t foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'AQ'
					print(f"leu caracter u foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'AQ'
					print(f"leu caracter v foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'AQ'
					print(f"leu caracter w foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'AQ'
					print(f"leu caracter x foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'AQ'
					print(f"leu caracter y foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'AQ'
					print(f"leu caracter z foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'AQ'
					print(f"leu caracter _ foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AQ'
					print(f"leu caracter < foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AQ'
					print(f"leu caracter - foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AQ'
					print(f"leu caracter + foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AQ'
					print(f"leu caracter / foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AQ'
					print(f"leu caracter * foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AQ'
					print(f"leu caracter ^ foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AQ'
					print(f"leu caracter > foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AR'
					print(f"leu caracter = foi para AR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AQ'
					print(f"leu caracter . foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AQ'
					print(f"leu caracter , foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AQ'
					print(f"leu caracter ; foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AQ'
					print(f"leu caracter : foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AQ'
					print(f"leu caracter ( foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AQ'
					print(f"leu caracter ) foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AQ'
					print(f"leu caracter [ foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AQ'
					print(f"leu caracter ] foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AQ'
					print(f"leu caracter \n foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AQ'
					print(f"leu caracter \t foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AQ'
					print(f"leu caracter   foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'AQ'
					print(f"leu caracter 0 foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'AQ'
					print(f"leu caracter 1 foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'AQ'
					print(f"leu caracter 2 foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'AQ'
					print(f"leu caracter 3 foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'AQ'
					print(f"leu caracter 4 foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'AQ'
					print(f"leu caracter 5 foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'AQ'
					print(f"leu caracter 6 foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'AQ'
					print(f"leu caracter 7 foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'AQ'
					print(f"leu caracter 8 foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'AQ'
					print(f"leu caracter 9 foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AQ'
					print(f"leu caracter \' foi para AQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AR':
				print('Tratar retorno estado final AR')
				print(f"Identificador montado {id}")
				state = 'A'
				print(id)
				print(c)
				tabelaSimbolos[id.strip()] = Atributo('',id.strip())
				return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'Y':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AS'
					print(f"leu caracter a foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'AS'
					print(f"leu caracter b foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'AS'
					print(f"leu caracter c foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'AS'
					print(f"leu caracter d foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'AS'
					print(f"leu caracter e foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'AS'
					print(f"leu caracter f foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'AS'
					print(f"leu caracter g foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'AS'
					print(f"leu caracter h foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'AS'
					print(f"leu caracter i foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'AS'
					print(f"leu caracter j foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'AS'
					print(f"leu caracter k foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'AS'
					print(f"leu caracter l foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'AS'
					print(f"leu caracter m foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'AS'
					print(f"leu caracter n foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'AS'
					print(f"leu caracter o foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'AS'
					print(f"leu caracter p foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'AS'
					print(f"leu caracter q foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'AS'
					print(f"leu caracter r foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'AS'
					print(f"leu caracter s foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'AS'
					print(f"leu caracter t foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'AS'
					print(f"leu caracter u foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'AS'
					print(f"leu caracter v foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'AS'
					print(f"leu caracter w foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'AS'
					print(f"leu caracter x foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'AS'
					print(f"leu caracter y foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'AS'
					print(f"leu caracter z foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'AS'
					print(f"leu caracter _ foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AS'
					print(f"leu caracter < foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AS'
					print(f"leu caracter - foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AS'
					print(f"leu caracter + foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AS'
					print(f"leu caracter / foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AS'
					print(f"leu caracter * foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AS'
					print(f"leu caracter ^ foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AS'
					print(f"leu caracter > foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AS'
					print(f"leu caracter = foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AS'
					print(f"leu caracter . foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AS'
					print(f"leu caracter , foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AS'
					print(f"leu caracter ; foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AS'
					print(f"leu caracter : foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AS'
					print(f"leu caracter ( foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AS'
					print(f"leu caracter ) foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AS'
					print(f"leu caracter [ foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AS'
					print(f"leu caracter ] foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'Y'
					print(f"leu caracter \n foi para Y linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'Y'
					print(f"leu caracter \t foi para Y linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'Y'
					print(f"leu caracter   foi para Y linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'AS'
					print(f"leu caracter 0 foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'AS'
					print(f"leu caracter 1 foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'AS'
					print(f"leu caracter 2 foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'AS'
					print(f"leu caracter 3 foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'AS'
					print(f"leu caracter 4 foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'AS'
					print(f"leu caracter 5 foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'AS'
					print(f"leu caracter 6 foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'AS'
					print(f"leu caracter 7 foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'AS'
					print(f"leu caracter 8 foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'AS'
					print(f"leu caracter 9 foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AS'
					print(f"leu caracter \' foi para AS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
					print(f"leu caracter a foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'AT'
					print(f"leu caracter b foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'AT'
					print(f"leu caracter c foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'AT'
					print(f"leu caracter d foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'AT'
					print(f"leu caracter e foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'AT'
					print(f"leu caracter f foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'AT'
					print(f"leu caracter g foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'AT'
					print(f"leu caracter h foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'AT'
					print(f"leu caracter i foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'AT'
					print(f"leu caracter j foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'AT'
					print(f"leu caracter k foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'AT'
					print(f"leu caracter l foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'AT'
					print(f"leu caracter m foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'AT'
					print(f"leu caracter n foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'AT'
					print(f"leu caracter o foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'AT'
					print(f"leu caracter p foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'AT'
					print(f"leu caracter q foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'AT'
					print(f"leu caracter r foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'AT'
					print(f"leu caracter s foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'AT'
					print(f"leu caracter t foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'AT'
					print(f"leu caracter u foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'AT'
					print(f"leu caracter v foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'AT'
					print(f"leu caracter w foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'AT'
					print(f"leu caracter x foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'AT'
					print(f"leu caracter y foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'AT'
					print(f"leu caracter z foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'AT'
					print(f"leu caracter _ foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AT'
					print(f"leu caracter < foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AT'
					print(f"leu caracter - foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AT'
					print(f"leu caracter + foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AT'
					print(f"leu caracter / foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AT'
					print(f"leu caracter * foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AT'
					print(f"leu caracter ^ foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AT'
					print(f"leu caracter > foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AT'
					print(f"leu caracter = foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AU'
					print(f"leu caracter . foi para AU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AT'
					print(f"leu caracter , foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AT'
					print(f"leu caracter ; foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AT'
					print(f"leu caracter : foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AT'
					print(f"leu caracter ( foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AT'
					print(f"leu caracter ) foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AT'
					print(f"leu caracter [ foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AT'
					print(f"leu caracter ] foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AT'
					print(f"leu caracter \n foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AT'
					print(f"leu caracter \t foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AT'
					print(f"leu caracter   foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'Z'
					print(f"leu caracter 0 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'Z'
					print(f"leu caracter 1 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'Z'
					print(f"leu caracter 2 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'Z'
					print(f"leu caracter 3 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'Z'
					print(f"leu caracter 4 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'Z'
					print(f"leu caracter 5 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'Z'
					print(f"leu caracter 6 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'Z'
					print(f"leu caracter 7 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'Z'
					print(f"leu caracter 8 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'Z'
					print(f"leu caracter 9 foi para Z linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AT'
					print(f"leu caracter \' foi para AT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AA':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AV'
					print(f"leu caracter a foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'AV'
					print(f"leu caracter b foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'AV'
					print(f"leu caracter c foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'AV'
					print(f"leu caracter d foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'AV'
					print(f"leu caracter e foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'AV'
					print(f"leu caracter f foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'AV'
					print(f"leu caracter g foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'AV'
					print(f"leu caracter h foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'AV'
					print(f"leu caracter i foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'AV'
					print(f"leu caracter j foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'AV'
					print(f"leu caracter k foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'AV'
					print(f"leu caracter l foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'AV'
					print(f"leu caracter m foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'AV'
					print(f"leu caracter n foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'AV'
					print(f"leu caracter o foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'AV'
					print(f"leu caracter p foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'AV'
					print(f"leu caracter q foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'AV'
					print(f"leu caracter r foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'AV'
					print(f"leu caracter s foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'AV'
					print(f"leu caracter t foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'AV'
					print(f"leu caracter u foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'AV'
					print(f"leu caracter v foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'AV'
					print(f"leu caracter w foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'AV'
					print(f"leu caracter x foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'AV'
					print(f"leu caracter y foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'AV'
					print(f"leu caracter z foi para AV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'ER'
					print(f"leu caracter _ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'ER'
					print(f"leu caracter < foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'ER'
					print(f"leu caracter - foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'ER'
					print(f"leu caracter + foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'ER'
					print(f"leu caracter / foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'ER'
					print(f"leu caracter * foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'ER'
					print(f"leu caracter ^ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'ER'
					print(f"leu caracter > foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'ER'
					print(f"leu caracter = foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'ER'
					print(f"leu caracter . foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'ER'
					print(f"leu caracter , foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'ER'
					print(f"leu caracter ; foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'ER'
					print(f"leu caracter : foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'ER'
					print(f"leu caracter ( foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'ER'
					print(f"leu caracter ) foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'ER'
					print(f"leu caracter [ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'ER'
					print(f"leu caracter ] foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'ER'
					print(f"leu caracter \n foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'ER'
					print(f"leu caracter \t foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'ER'
					print(f"leu caracter   foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'ER'
					print(f"leu caracter 0 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'ER'
					print(f"leu caracter 1 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'ER'
					print(f"leu caracter 2 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'ER'
					print(f"leu caracter 3 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'ER'
					print(f"leu caracter 4 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'ER'
					print(f"leu caracter 5 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'ER'
					print(f"leu caracter 6 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'ER'
					print(f"leu caracter 7 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'ER'
					print(f"leu caracter 8 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'ER'
					print(f"leu caracter 9 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'ER'
					print(f"leu caracter \' foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AB':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'AW'
					print(f"leu caracter e foi para AW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AD':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AY'
					print(f"leu caracter a foi para AY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AE':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AY'
					print(f"leu caracter a foi para AY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'AX'
					print(f"leu caracter q foi para AX linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'AZ'
					print(f"leu caracter t foi para AZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AF':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'BA'
					print(f"leu caracter c foi para BA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AG':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'BB'
					print(f"leu caracter m foi para BB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AH':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'BC'
					print(f"leu caracter o foi para BC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AI':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'BD'
					print(f"leu caracter i foi para BD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'BE'
					print(f"leu caracter t foi para BE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AJ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'BF'
					print(f"leu caracter o foi para BF linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AK':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'BG'
					print(f"leu caracter p foi para BG linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AL':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'BH'
					print(f"leu caracter n foi para BH linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'BI'
					print(f"leu caracter < foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'BI'
					print(f"leu caracter - foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'BI'
					print(f"leu caracter + foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'BI'
					print(f"leu caracter / foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'BI'
					print(f"leu caracter * foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'BI'
					print(f"leu caracter ^ foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'BI'
					print(f"leu caracter > foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'BI'
					print(f"leu caracter = foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'BI'
					print(f"leu caracter . foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'BI'
					print(f"leu caracter , foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'BI'
					print(f"leu caracter ; foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'BI'
					print(f"leu caracter : foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'BI'
					print(f"leu caracter ( foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'BI'
					print(f"leu caracter ) foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'BI'
					print(f"leu caracter [ foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'BI'
					print(f"leu caracter ] foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'BI'
					print(f"leu caracter \n foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'BI'
					print(f"leu caracter \t foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'BI'
					print(f"leu caracter   foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'BI'
					print(f"leu caracter \' foi para BI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AN':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == '-':
					state = 'BJ'
					print(f"leu caracter - foi para BJ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					print('Tratar retorno estado final BI')
					print(f"Identificador montado {id}")
					state = 'A'
					lerProx = False
					if c not in ['\n', '\t', ' ','+','-','/',',','*',':',';','(',')','=']:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
					elif c in ['\n', '\t', ' ',';',')','+']:
						tabelaSimbolos[id] = Atributo('',id)
						return Token(id,'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AU':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'ER'
					print(f"leu caracter a foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'ER'
					print(f"leu caracter b foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'ER'
					print(f"leu caracter c foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'ER'
					print(f"leu caracter d foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'ER'
					print(f"leu caracter e foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'ER'
					print(f"leu caracter f foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'ER'
					print(f"leu caracter g foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'ER'
					print(f"leu caracter h foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'ER'
					print(f"leu caracter i foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'ER'
					print(f"leu caracter j foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'ER'
					print(f"leu caracter k foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'ER'
					print(f"leu caracter l foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'ER'
					print(f"leu caracter m foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'ER'
					print(f"leu caracter n foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'ER'
					print(f"leu caracter o foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'ER'
					print(f"leu caracter p foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'ER'
					print(f"leu caracter q foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'ER'
					print(f"leu caracter r foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'ER'
					print(f"leu caracter s foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'ER'
					print(f"leu caracter t foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'ER'
					print(f"leu caracter u foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'ER'
					print(f"leu caracter v foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'ER'
					print(f"leu caracter w foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'ER'
					print(f"leu caracter x foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'ER'
					print(f"leu caracter y foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'ER'
					print(f"leu caracter z foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'ER'
					print(f"leu caracter _ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'ER'
					print(f"leu caracter < foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'ER'
					print(f"leu caracter - foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'ER'
					print(f"leu caracter + foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'ER'
					print(f"leu caracter / foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'ER'
					print(f"leu caracter * foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'ER'
					print(f"leu caracter ^ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'ER'
					print(f"leu caracter > foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'ER'
					print(f"leu caracter = foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'ER'
					print(f"leu caracter . foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'ER'
					print(f"leu caracter , foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'ER'
					print(f"leu caracter ; foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'ER'
					print(f"leu caracter : foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'ER'
					print(f"leu caracter ( foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'ER'
					print(f"leu caracter ) foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'ER'
					print(f"leu caracter [ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'ER'
					print(f"leu caracter ] foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'ER'
					print(f"leu caracter \n foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'ER'
					print(f"leu caracter \t foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'ER'
					print(f"leu caracter   foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'BK'
					print(f"leu caracter 0 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'BK'
					print(f"leu caracter 1 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'BK'
					print(f"leu caracter 2 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'BK'
					print(f"leu caracter 3 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'BK'
					print(f"leu caracter 4 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'BK'
					print(f"leu caracter 5 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'BK'
					print(f"leu caracter 6 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'BK'
					print(f"leu caracter 7 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'BK'
					print(f"leu caracter 8 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'BK'
					print(f"leu caracter 9 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'ER'
					print(f"leu caracter \' foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AV':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'ER'
					print(f"leu caracter a foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'ER'
					print(f"leu caracter b foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'ER'
					print(f"leu caracter c foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'ER'
					print(f"leu caracter d foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'ER'
					print(f"leu caracter e foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'ER'
					print(f"leu caracter f foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'ER'
					print(f"leu caracter g foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'ER'
					print(f"leu caracter h foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'ER'
					print(f"leu caracter i foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'ER'
					print(f"leu caracter j foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'ER'
					print(f"leu caracter k foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'ER'
					print(f"leu caracter l foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'ER'
					print(f"leu caracter m foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'ER'
					print(f"leu caracter n foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'ER'
					print(f"leu caracter o foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'ER'
					print(f"leu caracter p foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'ER'
					print(f"leu caracter q foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'ER'
					print(f"leu caracter r foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'ER'
					print(f"leu caracter s foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'ER'
					print(f"leu caracter t foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'ER'
					print(f"leu caracter u foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'ER'
					print(f"leu caracter v foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'ER'
					print(f"leu caracter w foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'ER'
					print(f"leu caracter x foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'ER'
					print(f"leu caracter y foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'ER'
					print(f"leu caracter z foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'ER'
					print(f"leu caracter _ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'ER'
					print(f"leu caracter < foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'ER'
					print(f"leu caracter - foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'ER'
					print(f"leu caracter + foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'ER'
					print(f"leu caracter / foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'ER'
					print(f"leu caracter * foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'ER'
					print(f"leu caracter ^ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'ER'
					print(f"leu caracter > foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'ER'
					print(f"leu caracter = foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'ER'
					print(f"leu caracter . foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'ER'
					print(f"leu caracter , foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'ER'
					print(f"leu caracter ; foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'ER'
					print(f"leu caracter : foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'ER'
					print(f"leu caracter ( foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'ER'
					print(f"leu caracter ) foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'ER'
					print(f"leu caracter [ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'ER'
					print(f"leu caracter ] foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'ER'
					print(f"leu caracter \n foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'ER'
					print(f"leu caracter \t foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'ER'
					print(f"leu caracter   foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'ER'
					print(f"leu caracter 0 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'ER'
					print(f"leu caracter 1 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'ER'
					print(f"leu caracter 2 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'ER'
					print(f"leu caracter 3 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'ER'
					print(f"leu caracter 4 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'ER'
					print(f"leu caracter 5 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'ER'
					print(f"leu caracter 6 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'ER'
					print(f"leu caracter 7 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'ER'
					print(f"leu caracter 8 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'ER'
					print(f"leu caracter 9 foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'BL'
					print(f"leu caracter \' foi para BL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AW':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'BM'
					print(f"leu caracter < foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'BM'
					print(f"leu caracter - foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'BM'
					print(f"leu caracter + foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'BM'
					print(f"leu caracter / foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'BM'
					print(f"leu caracter * foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'BM'
					print(f"leu caracter ^ foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'BM'
					print(f"leu caracter > foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'BM'
					print(f"leu caracter = foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'BM'
					print(f"leu caracter . foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'BM'
					print(f"leu caracter , foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'BM'
					print(f"leu caracter ; foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'BM'
					print(f"leu caracter : foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'BM'
					print(f"leu caracter ( foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'BM'
					print(f"leu caracter ) foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'BM'
					print(f"leu caracter [ foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'BM'
					print(f"leu caracter ] foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'BM'
					print(f"leu caracter \n foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'BM'
					print(f"leu caracter \t foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'BM'
					print(f"leu caracter   foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'BM'
					print(f"leu caracter \' foi para BM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'AY':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'BN'
					print(f"leu caracter r foi para BN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AX':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'BO'
					print(f"leu caracter u foi para BO linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AZ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'AZZ'
					print(f"leu caracter a foi para AZZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'AZZ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'BP'
					print(f"leu caracter o foi para BP linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'C'
					print(f"leu caracter < foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'C'
					print(f"leu caracter - foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'C'
					print(f"leu caracter + foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'C'
					print(f"leu caracter / foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'C'
					print(f"leu caracter * foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'C'
					print(f"leu caracter ^ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'C'
					print(f"leu caracter > foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'C'
					print(f"leu caracter = foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'C'
					print(f"leu caracter . foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'C'
					print(f"leu caracter , foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'C'
					print(f"leu caracter ; foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'C'
					print(f"leu caracter ( foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'C'
					print(f"leu caracter ) foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'C'
					print(f"leu caracter [ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'X'
					print(f"leu caracter ] foi para X linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'C'
					print(f"leu caracter \n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'C'
					print(f"leu caracter \t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'C'
					print(f"leu caracter   foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'C'
					print(f"leu caracter \' foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BA':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'BQ'
					print(f"leu caracter a foi para BQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BB':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'BR'
					print(f"leu caracter < foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'BR'
					print(f"leu caracter - foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'BR'
					print(f"leu caracter + foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'BR'
					print(f"leu caracter / foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'BR'
					print(f"leu caracter * foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'BR'
					print(f"leu caracter ^ foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'BR'
					print(f"leu caracter > foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'BR'
					print(f"leu caracter = foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'BR'
					print(f"leu caracter . foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'BR'
					print(f"leu caracter , foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'BR'
					print(f"leu caracter ; foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'BR'
					print(f"leu caracter : foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'BR'
					print(f"leu caracter ( foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'BR'
					print(f"leu caracter ) foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'BR'
					print(f"leu caracter [ foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'BR'
					print(f"leu caracter ] foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'BR'
					print(f"leu caracter \n foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'BR'
					print(f"leu caracter \t foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'BR'
					print(f"leu caracter   foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'BR'
					print(f"leu caracter \' foi para BR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'BC':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'BS'
					print(f"leu caracter a foi para BS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BD':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'BT'
					print(f"leu caracter c foi para BT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BE':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'BU'
					print(f"leu caracter < foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'BU'
					print(f"leu caracter - foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'BU'
					print(f"leu caracter + foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'BU'
					print(f"leu caracter / foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'BU'
					print(f"leu caracter * foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'BU'
					print(f"leu caracter ^ foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'BU'
					print(f"leu caracter > foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'BU'
					print(f"leu caracter = foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'BU'
					print(f"leu caracter . foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'BU'
					print(f"leu caracter , foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'BU'
					print(f"leu caracter ; foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'BU'
					print(f"leu caracter : foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'BU'
					print(f"leu caracter ( foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'BU'
					print(f"leu caracter ) foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'BU'
					print(f"leu caracter [ foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'BU'
					print(f"leu caracter ] foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'BU'
					print(f"leu caracter \n foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'BU'
					print(f"leu caracter \t foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'BU'
					print(f"leu caracter   foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'BU'
					print(f"leu caracter \' foi para BU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'BF':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'BV'
					print(f"leu caracter g foi para BV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BG':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'BW'
					print(f"leu caracter i foi para BW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BH':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'BX'
					print(f"leu caracter o foi para BX linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BJ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'BY'
					print(f"leu caracter a foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'BY'
					print(f"leu caracter b foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'BY'
					print(f"leu caracter c foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'BY'
					print(f"leu caracter d foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'BY'
					print(f"leu caracter e foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'BY'
					print(f"leu caracter f foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'BY'
					print(f"leu caracter g foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'BY'
					print(f"leu caracter h foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'BY'
					print(f"leu caracter i foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'BY'
					print(f"leu caracter j foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'BY'
					print(f"leu caracter k foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'BY'
					print(f"leu caracter l foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'BY'
					print(f"leu caracter m foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'BY'
					print(f"leu caracter n foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'BY'
					print(f"leu caracter o foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'BY'
					print(f"leu caracter p foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'BY'
					print(f"leu caracter q foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'BY'
					print(f"leu caracter r foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'BY'
					print(f"leu caracter s foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'BY'
					print(f"leu caracter t foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'BY'
					print(f"leu caracter u foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'BY'
					print(f"leu caracter v foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'BY'
					print(f"leu caracter w foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'BY'
					print(f"leu caracter x foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'BY'
					print(f"leu caracter y foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'BY'
					print(f"leu caracter z foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'BY'
					print(f"leu caracter _ foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'BY'
					print(f"leu caracter < foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'BY'
					print(f"leu caracter - foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'BY'
					print(f"leu caracter + foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'BY'
					print(f"leu caracter / foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'BY'
					print(f"leu caracter * foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'BY'
					print(f"leu caracter ^ foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'BY'
					print(f"leu caracter > foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'BY'
					print(f"leu caracter = foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'BY'
					print(f"leu caracter . foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'BY'
					print(f"leu caracter , foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'BY'
					print(f"leu caracter ; foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'BY'
					print(f"leu caracter : foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'BY'
					print(f"leu caracter ( foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'BY'
					print(f"leu caracter ) foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'BY'
					print(f"leu caracter [ foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'BY'
					print(f"leu caracter ] foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'BY'
					print(f"leu caracter \n foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'BY'
					print(f"leu caracter \t foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'BY'
					print(f"leu caracter   foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'BY'
					print(f"leu caracter 0 foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'BY'
					print(f"leu caracter 1 foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'BY'
					print(f"leu caracter 2 foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'BY'
					print(f"leu caracter 3 foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'BY'
					print(f"leu caracter 4 foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'BY'
					print(f"leu caracter 5 foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'BY'
					print(f"leu caracter 6 foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'BY'
					print(f"leu caracter 7 foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'BY'
					print(f"leu caracter 8 foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'BY'
					print(f"leu caracter 9 foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'BY'
					print(f"leu caracter \' foi para BY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'BK':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'CA'
					print(f"leu caracter a foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'CA'
					print(f"leu caracter b foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'CA'
					print(f"leu caracter c foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'CA'
					print(f"leu caracter d foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'BZ'
					print(f"leu caracter e foi para BZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'CA'
					print(f"leu caracter f foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'CA'
					print(f"leu caracter g foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'CA'
					print(f"leu caracter h foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'CA'
					print(f"leu caracter i foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'CA'
					print(f"leu caracter j foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'CA'
					print(f"leu caracter k foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'CA'
					print(f"leu caracter l foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'CA'
					print(f"leu caracter m foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'CA'
					print(f"leu caracter n foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'CA'
					print(f"leu caracter o foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'CA'
					print(f"leu caracter p foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'CA'
					print(f"leu caracter q foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'CA'
					print(f"leu caracter r foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'CA'
					print(f"leu caracter s foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'CA'
					print(f"leu caracter t foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'CA'
					print(f"leu caracter u foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'CA'
					print(f"leu caracter v foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'CA'
					print(f"leu caracter w foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'CA'
					print(f"leu caracter x foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'CA'
					print(f"leu caracter y foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'CA'
					print(f"leu caracter z foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'CA'
					print(f"leu caracter _ foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'CA'
					print(f"leu caracter < foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'CA'
					print(f"leu caracter - foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'CA'
					print(f"leu caracter + foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'CA'
					print(f"leu caracter / foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'CA'
					print(f"leu caracter * foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'CA'
					print(f"leu caracter ^ foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'CA'
					print(f"leu caracter > foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'CA'
					print(f"leu caracter = foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'CA'
					print(f"leu caracter . foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'CA'
					print(f"leu caracter , foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'CA'
					print(f"leu caracter ; foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'CA'
					print(f"leu caracter : foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'CA'
					print(f"leu caracter ( foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'CA'
					print(f"leu caracter ) foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'CA'
					print(f"leu caracter [ foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'CA'
					print(f"leu caracter ] foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'CA'
					print(f"leu caracter \n foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'CA'
					print(f"leu caracter \t foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'CA'
					print(f"leu caracter   foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'BK'
					print(f"leu caracter 0 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'BK'
					print(f"leu caracter 1 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'BK'
					print(f"leu caracter 2 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'BK'
					print(f"leu caracter 3 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'BK'
					print(f"leu caracter 4 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'BK'
					print(f"leu caracter 5 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'BK'
					print(f"leu caracter 6 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'BK'
					print(f"leu caracter 7 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'BK'
					print(f"leu caracter 8 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'BK'
					print(f"leu caracter 9 foi para BK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'CA'
					print(f"leu caracter \' foi para CA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'BM':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BN':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'CB'
					print(f"leu caracter < foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'CB'
					print(f"leu caracter - foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'CB'
					print(f"leu caracter + foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'CB'
					print(f"leu caracter / foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'CB'
					print(f"leu caracter * foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'CB'
					print(f"leu caracter ^ foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'CB'
					print(f"leu caracter > foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'CB'
					print(f"leu caracter = foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'CB'
					print(f"leu caracter . foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'CB'
					print(f"leu caracter , foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'CB'
					print(f"leu caracter ; foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'CB'
					print(f"leu caracter : foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'CB'
					print(f"leu caracter ( foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'CB'
					print(f"leu caracter ) foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'CB'
					print(f"leu caracter [ foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'CB'
					print(f"leu caracter ] foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'CB'
					print(f"leu caracter \n foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'CB'
					print(f"leu caracter \t foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'CB'
					print(f"leu caracter   foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'CB'
					print(f"leu caracter \' foi para CB linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'BO':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'CC'
					print(f"leu caracter a foi para CC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BP':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'CD'
					print(f"leu caracter < foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'CD'
					print(f"leu caracter - foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'CD'
					print(f"leu caracter + foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'CD'
					print(f"leu caracter / foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'CD'
					print(f"leu caracter * foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'CD'
					print(f"leu caracter ^ foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'CD'
					print(f"leu caracter > foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'CD'
					print(f"leu caracter = foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'CD'
					print(f"leu caracter . foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'CD'
					print(f"leu caracter , foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'CD'
					print(f"leu caracter ; foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'CD'
					print(f"leu caracter : foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'CD'
					print(f"leu caracter ( foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'CD'
					print(f"leu caracter ) foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'CD'
					print(f"leu caracter [ foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'CD'
					print(f"leu caracter ] foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'CD'
					print(f"leu caracter \n foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'CD'
					print(f"leu caracter \t foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'CD'
					print(f"leu caracter   foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'CD'
					print(f"leu caracter \' foi para CD linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'BQ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'CE'
					print(f"leu caracter < foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'CE'
					print(f"leu caracter - foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'CE'
					print(f"leu caracter + foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'CE'
					print(f"leu caracter / foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'CE'
					print(f"leu caracter * foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'CE'
					print(f"leu caracter ^ foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'CE'
					print(f"leu caracter > foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'CE'
					print(f"leu caracter = foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'CE'
					print(f"leu caracter . foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'CE'
					print(f"leu caracter , foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'CE'
					print(f"leu caracter ; foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'CE'
					print(f"leu caracter : foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'CE'
					print(f"leu caracter ( foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'CE'
					print(f"leu caracter ) foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'CE'
					print(f"leu caracter [ foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'CE'
					print(f"leu caracter ] foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'CE'
					print(f"leu caracter \n foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'CE'
					print(f"leu caracter \t foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'CE'
					print(f"leu caracter   foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'CE'
					print(f"leu caracter \' foi para CE linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'BS':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'CF'
					print(f"leu caracter t foi para CF linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BT':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'CG'
					print(f"leu caracter i foi para CG linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BV':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'CH'
					print(f"leu caracter r foi para CH linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BW':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'CI'
					print(f"leu caracter t foi para CI linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BX':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'CJ'
					print(f"leu caracter o foi para CJ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'BZ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'ER'
					print(f"leu caracter a foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'ER'
					print(f"leu caracter b foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'ER'
					print(f"leu caracter c foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'ER'
					print(f"leu caracter d foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'ER'
					print(f"leu caracter e foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'ER'
					print(f"leu caracter f foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'ER'
					print(f"leu caracter g foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'ER'
					print(f"leu caracter h foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'ER'
					print(f"leu caracter i foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'ER'
					print(f"leu caracter j foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'ER'
					print(f"leu caracter k foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'ER'
					print(f"leu caracter l foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'ER'
					print(f"leu caracter m foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'ER'
					print(f"leu caracter n foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'ER'
					print(f"leu caracter o foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'ER'
					print(f"leu caracter p foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'ER'
					print(f"leu caracter q foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'ER'
					print(f"leu caracter r foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'ER'
					print(f"leu caracter s foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'ER'
					print(f"leu caracter t foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'ER'
					print(f"leu caracter u foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'ER'
					print(f"leu caracter v foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'ER'
					print(f"leu caracter w foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'ER'
					print(f"leu caracter x foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'ER'
					print(f"leu caracter y foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'ER'
					print(f"leu caracter z foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'ER'
					print(f"leu caracter _ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'ER'
					print(f"leu caracter < foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'CK'
					print(f"leu caracter - foi para CK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'CK'
					print(f"leu caracter + foi para CK linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'ER'
					print(f"leu caracter / foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'ER'
					print(f"leu caracter * foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'ER'
					print(f"leu caracter ^ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'ER'
					print(f"leu caracter > foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'ER'
					print(f"leu caracter = foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'ER'
					print(f"leu caracter . foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'ER'
					print(f"leu caracter , foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'ER'
					print(f"leu caracter ; foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'ER'
					print(f"leu caracter : foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'ER'
					print(f"leu caracter ( foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'ER'
					print(f"leu caracter ) foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'ER'
					print(f"leu caracter [ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'ER'
					print(f"leu caracter ] foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'ER'
					print(f"leu caracter \n foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'ER'
					print(f"leu caracter \t foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'ER'
					print(f"leu caracter   foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'CL'
					print(f"leu caracter 0 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'CL'
					print(f"leu caracter 1 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'CL'
					print(f"leu caracter 2 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'CL'
					print(f"leu caracter 3 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'CL'
					print(f"leu caracter 4 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'CL'
					print(f"leu caracter 5 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'CL'
					print(f"leu caracter 6 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'CL'
					print(f"leu caracter 7 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'CL'
					print(f"leu caracter 8 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'CL'
					print(f"leu caracter 9 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'ER'
					print(f"leu caracter \' foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CC':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'CM'
					print(f"leu caracter n foi para CM linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CF':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'CN'
					print(f"leu caracter < foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'CN'
					print(f"leu caracter - foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'CN'
					print(f"leu caracter + foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'CN'
					print(f"leu caracter / foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'CN'
					print(f"leu caracter * foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'CN'
					print(f"leu caracter ^ foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'CN'
					print(f"leu caracter > foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'CN'
					print(f"leu caracter = foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'CN'
					print(f"leu caracter . foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'CN'
					print(f"leu caracter , foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'CN'
					print(f"leu caracter ; foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'CN'
					print(f"leu caracter : foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'CN'
					print(f"leu caracter ( foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'CN'
					print(f"leu caracter ) foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'CN'
					print(f"leu caracter [ foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'CN'
					print(f"leu caracter ] foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'CN'
					print(f"leu caracter \n foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'CN'
					print(f"leu caracter \t foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'CN'
					print(f"leu caracter   foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'CN'
					print(f"leu caracter \' foi para CN linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'CG':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'CO'
					print(f"leu caracter o foi para CO linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CH':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'CP'
					print(f"leu caracter a foi para CP linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CI':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'CQ'
					print(f"leu caracter a foi para CQ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CJ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'CR'
					print(f"leu caracter < foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'CR'
					print(f"leu caracter - foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'CR'
					print(f"leu caracter + foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'CR'
					print(f"leu caracter / foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'CR'
					print(f"leu caracter * foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'CR'
					print(f"leu caracter ^ foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'CR'
					print(f"leu caracter > foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'CR'
					print(f"leu caracter = foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'CR'
					print(f"leu caracter . foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'CR'
					print(f"leu caracter , foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'CR'
					print(f"leu caracter ; foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'CR'
					print(f"leu caracter : foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'CR'
					print(f"leu caracter ( foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'CR'
					print(f"leu caracter ) foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'CR'
					print(f"leu caracter [ foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'CR'
					print(f"leu caracter ] foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'CR'
					print(f"leu caracter \n foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'CR'
					print(f"leu caracter \t foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'CR'
					print(f"leu caracter   foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'CR'
					print(f"leu caracter \' foi para CR linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'CK':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'ER'
					print(f"leu caracter a foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'ER'
					print(f"leu caracter b foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'ER'
					print(f"leu caracter c foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'ER'
					print(f"leu caracter d foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'ER'
					print(f"leu caracter e foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'ER'
					print(f"leu caracter f foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'ER'
					print(f"leu caracter g foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'ER'
					print(f"leu caracter h foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'ER'
					print(f"leu caracter i foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'ER'
					print(f"leu caracter j foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'ER'
					print(f"leu caracter k foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'ER'
					print(f"leu caracter l foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'ER'
					print(f"leu caracter m foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'ER'
					print(f"leu caracter n foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'ER'
					print(f"leu caracter o foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'ER'
					print(f"leu caracter p foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'ER'
					print(f"leu caracter q foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'ER'
					print(f"leu caracter r foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'ER'
					print(f"leu caracter s foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'ER'
					print(f"leu caracter t foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'ER'
					print(f"leu caracter u foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'ER'
					print(f"leu caracter v foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'ER'
					print(f"leu caracter w foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'ER'
					print(f"leu caracter x foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'ER'
					print(f"leu caracter y foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'ER'
					print(f"leu caracter z foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'ER'
					print(f"leu caracter _ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'ER'
					print(f"leu caracter < foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'ER'
					print(f"leu caracter - foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'ER'
					print(f"leu caracter + foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'ER'
					print(f"leu caracter / foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'ER'
					print(f"leu caracter * foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'ER'
					print(f"leu caracter ^ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'ER'
					print(f"leu caracter > foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'ER'
					print(f"leu caracter = foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'ER'
					print(f"leu caracter . foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'ER'
					print(f"leu caracter , foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'ER'
					print(f"leu caracter ; foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'ER'
					print(f"leu caracter : foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'ER'
					print(f"leu caracter ( foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'ER'
					print(f"leu caracter ) foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'ER'
					print(f"leu caracter [ foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'ER'
					print(f"leu caracter ] foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'ER'
					print(f"leu caracter \n foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'ER'
					print(f"leu caracter \t foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'ER'
					print(f"leu caracter   foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'CL'
					print(f"leu caracter 0 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'CL'
					print(f"leu caracter 1 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'CL'
					print(f"leu caracter 2 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'CL'
					print(f"leu caracter 3 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'CL'
					print(f"leu caracter 4 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'CL'
					print(f"leu caracter 5 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'CL'
					print(f"leu caracter 6 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'CL'
					print(f"leu caracter 7 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'CL'
					print(f"leu caracter 8 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'CL'
					print(f"leu caracter 9 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'ER'
					print(f"leu caracter \' foi para ER linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CL':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'CS'
					print(f"leu caracter a foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'CS'
					print(f"leu caracter b foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'CS'
					print(f"leu caracter c foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'CS'
					print(f"leu caracter d foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'CS'
					print(f"leu caracter e foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'CS'
					print(f"leu caracter f foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'CS'
					print(f"leu caracter g foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'CS'
					print(f"leu caracter h foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'CS'
					print(f"leu caracter i foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'CS'
					print(f"leu caracter j foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'CS'
					print(f"leu caracter k foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'CS'
					print(f"leu caracter l foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'CS'
					print(f"leu caracter m foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'CS'
					print(f"leu caracter n foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'CS'
					print(f"leu caracter o foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'CS'
					print(f"leu caracter p foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'CS'
					print(f"leu caracter q foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'CS'
					print(f"leu caracter r foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'CS'
					print(f"leu caracter s foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'CS'
					print(f"leu caracter t foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'CS'
					print(f"leu caracter u foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'CS'
					print(f"leu caracter v foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'CS'
					print(f"leu caracter w foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'CS'
					print(f"leu caracter x foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'CS'
					print(f"leu caracter y foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'CS'
					print(f"leu caracter z foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'CS'
					print(f"leu caracter _ foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'CS'
					print(f"leu caracter < foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'CS'
					print(f"leu caracter - foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'CS'
					print(f"leu caracter + foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'CS'
					print(f"leu caracter / foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'CS'
					print(f"leu caracter * foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'CS'
					print(f"leu caracter ^ foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'CS'
					print(f"leu caracter > foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'CS'
					print(f"leu caracter = foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'CS'
					print(f"leu caracter . foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'CS'
					print(f"leu caracter , foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'CS'
					print(f"leu caracter ; foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'CS'
					print(f"leu caracter : foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'CS'
					print(f"leu caracter ( foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'CS'
					print(f"leu caracter ) foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'CS'
					print(f"leu caracter [ foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'CS'
					print(f"leu caracter ] foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'CS'
					print(f"leu caracter \n foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'CS'
					print(f"leu caracter \t foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'CS'
					print(f"leu caracter   foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'CL'
					print(f"leu caracter 0 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'CL'
					print(f"leu caracter 1 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'CL'
					print(f"leu caracter 2 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'CL'
					print(f"leu caracter 3 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'CL'
					print(f"leu caracter 4 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'CL'
					print(f"leu caracter 5 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'CL'
					print(f"leu caracter 6 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'CL'
					print(f"leu caracter 7 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'CL'
					print(f"leu caracter 8 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'CL'
					print(f"leu caracter 9 foi para CL linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'CS'
					print(f"leu caracter \' foi para CS linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'CM':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'CV'
					print(f"leu caracter m foi para CV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'CT'
					print(f"leu caracter t foi para CT linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CO':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'CU'
					print(f"leu caracter < foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'CU'
					print(f"leu caracter - foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'CU'
					print(f"leu caracter + foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'CU'
					print(f"leu caracter / foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'CU'
					print(f"leu caracter * foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'CU'
					print(f"leu caracter ^ foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'CU'
					print(f"leu caracter > foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'CU'
					print(f"leu caracter = foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'CU'
					print(f"leu caracter . foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'CU'
					print(f"leu caracter , foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'CU'
					print(f"leu caracter ; foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'CU'
					print(f"leu caracter : foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'CU'
					print(f"leu caracter ( foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'CU'
					print(f"leu caracter ) foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'CU'
					print(f"leu caracter [ foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'CU'
					print(f"leu caracter ] foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'CU'
					print(f"leu caracter \n foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'CU'
					print(f"leu caracter \t foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'CU'
					print(f"leu caracter   foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'CU'
					print(f"leu caracter \' foi para CU linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'CP':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'CV'
					print(f"leu caracter m foi para CV linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CQ':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'CW'
					print(f"leu caracter < foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'CW'
					print(f"leu caracter - foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'CW'
					print(f"leu caracter + foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'CW'
					print(f"leu caracter / foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'CW'
					print(f"leu caracter * foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'CW'
					print(f"leu caracter ^ foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'CW'
					print(f"leu caracter > foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'CW'
					print(f"leu caracter = foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'CW'
					print(f"leu caracter . foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'CW'
					print(f"leu caracter , foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'CW'
					print(f"leu caracter ; foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'CW'
					print(f"leu caracter : foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'CW'
					print(f"leu caracter ( foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'CW'
					print(f"leu caracter ) foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'CW'
					print(f"leu caracter [ foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'CW'
					print(f"leu caracter ] foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'CW'
					print(f"leu caracter \n foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'CW'
					print(f"leu caracter \t foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'CW'
					print(f"leu caracter   foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'CW'
					print(f"leu caracter \' foi para CW linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'CT':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'CX'
					print(f"leu caracter o foi para CX linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CV':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'CY'
					print(f"leu caracter a foi para CY linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'AC'
					print(f"leu caracter < foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'AC'
					print(f"leu caracter - foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'AC'
					print(f"leu caracter + foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'AC'
					print(f"leu caracter / foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'AC'
					print(f"leu caracter * foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'AC'
					print(f"leu caracter ^ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'AC'
					print(f"leu caracter > foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'AC'
					print(f"leu caracter = foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'AC'
					print(f"leu caracter . foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'AC'
					print(f"leu caracter , foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'AC'
					print(f"leu caracter ; foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'AC'
					print(f"leu caracter : foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'AC'
					print(f"leu caracter ( foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'AC'
					print(f"leu caracter ) foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'AC'
					print(f"leu caracter [ foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'AC'
					print(f"leu caracter ] foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'AC'
					print(f"leu caracter \n foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'AC'
					print(f"leu caracter \t foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'AC'
					print(f"leu caracter   foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'AC'
					print(f"leu caracter \' foi para AC linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				else:
					state = 'ER'
					return Token('Erro',f"Erro - caracter {c} nao e reconhecido",linhaGlobal,coluna)
			case 'CX':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'CZ'
					print(f"leu caracter < foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'CZ'
					print(f"leu caracter - foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'CZ'
					print(f"leu caracter + foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'CZ'
					print(f"leu caracter / foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'CZ'
					print(f"leu caracter * foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'CZ'
					print(f"leu caracter ^ foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'CZ'
					print(f"leu caracter > foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'CZ'
					print(f"leu caracter = foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'CZ'
					print(f"leu caracter . foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'CZ'
					print(f"leu caracter , foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'CZ'
					print(f"leu caracter ; foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'CZ'
					print(f"leu caracter : foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'CZ'
					print(f"leu caracter ( foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'CZ'
					print(f"leu caracter ) foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'CZ'
					print(f"leu caracter [ foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'CZ'
					print(f"leu caracter ] foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'CZ'
					print(f"leu caracter \n foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'CZ'
					print(f"leu caracter \t foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'CZ'
					print(f"leu caracter   foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'CZ'
					print(f"leu caracter \' foi para CZ linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
					tabelaSimbolos[id[:-1]] = Atributo('',id[:-1])
					return Token(id[:-1],'ATRIBUTO',linhaGlobal,coluna)
				elif c in [' ',';',')','+']:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
				else:
					print(id)
					print(c)
					if id != c:
						f.seek(f.tell()-1)
						tabelaSimbolos[id[:-1].strip()] = Atributo('',id[:-1].strip())
						return Token(id[:-1].strip(),'ATRIBUTO',linhaGlobal,coluna)
					else:
						tabelaSimbolos[id.strip()] = Atributo('',id.strip())
						return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)
			case 'CY':
				c = nextChar()
				id += c
				colunaGlobal += 1
				if c.lower() == 'a':
					state = 'C'
					print(f"leu caracter a foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'b':
					state = 'C'
					print(f"leu caracter b foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'c':
					state = 'C'
					print(f"leu caracter c foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'd':
					state = 'C'
					print(f"leu caracter d foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'e':
					state = 'C'
					print(f"leu caracter e foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'f':
					state = 'C'
					print(f"leu caracter f foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'g':
					state = 'C'
					print(f"leu caracter g foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'h':
					state = 'C'
					print(f"leu caracter h foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'i':
					state = 'C'
					print(f"leu caracter i foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'j':
					state = 'C'
					print(f"leu caracter j foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'k':
					state = 'C'
					print(f"leu caracter k foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'l':
					state = 'C'
					print(f"leu caracter l foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'm':
					state = 'C'
					print(f"leu caracter m foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'n':
					state = 'C'
					print(f"leu caracter n foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'o':
					state = 'C'
					print(f"leu caracter o foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'p':
					state = 'C'
					print(f"leu caracter p foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'q':
					state = 'C'
					print(f"leu caracter q foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'r':
					state = 'C'
					print(f"leu caracter r foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 's':
					state = 'C'
					print(f"leu caracter s foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 't':
					state = 'C'
					print(f"leu caracter t foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'u':
					state = 'C'
					print(f"leu caracter u foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'v':
					state = 'C'
					print(f"leu caracter v foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'w':
					state = 'C'
					print(f"leu caracter w foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'x':
					state = 'C'
					print(f"leu caracter x foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'y':
					state = 'C'
					print(f"leu caracter y foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == 'z':
					state = 'C'
					print(f"leu caracter z foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '_':
					state = 'C'
					print(f"leu caracter _ foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '<':
					state = 'DA'
					print(f"leu caracter < foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '-':
					state = 'DA'
					print(f"leu caracter - foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '+':
					state = 'DA'
					print(f"leu caracter + foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '/':
					state = 'DA'
					print(f"leu caracter / foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '*':
					state = 'DA'
					print(f"leu caracter * foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '^':
					state = 'DA'
					print(f"leu caracter ^ foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '>':
					state = 'DA'
					print(f"leu caracter > foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '=':
					state = 'DA'
					print(f"leu caracter = foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '.':
					state = 'DA'
					print(f"leu caracter . foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ',':
					state = 'DA'
					print(f"leu caracter , foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ';':
					state = 'DA'
					print(f"leu caracter ; foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ':':
					state = 'DA'
					print(f"leu caracter : foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '(':
					state = 'DA'
					print(f"leu caracter ( foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ')':
					state = 'DA'
					print(f"leu caracter ) foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '[':
					state = 'DA'
					print(f"leu caracter [ foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ']':
					state = 'DA'
					print(f"leu caracter ] foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\n':
					linhaGlobal += 1
					colunaGlobal = 0
					coluna = 0
					state = 'DA'
					print(f"leu caracter \n foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\t':
					state = 'DA'
					print(f"leu caracter \t foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == ' ':
					state = 'DA'
					print(f"leu caracter   foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '0':
					state = 'C'
					print(f"leu caracter 0 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '1':
					state = 'C'
					print(f"leu caracter 1 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '2':
					state = 'C'
					print(f"leu caracter 2 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '3':
					state = 'C'
					print(f"leu caracter 3 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '4':
					state = 'C'
					print(f"leu caracter 4 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '5':
					state = 'C'
					print(f"leu caracter 5 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '6':
					state = 'C'
					print(f"leu caracter 6 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '7':
					state = 'C'
					print(f"leu caracter 7 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '8':
					state = 'C'
					print(f"leu caracter 8 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '9':
					state = 'C'
					print(f"leu caracter 9 foi para C linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
				elif c.lower() == '\'':
					state = 'DA'
					print(f"leu caracter \' foi para DA linha {linhaGlobal} colunaG {colunaGlobal} coluna {coluna}")
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
				tabelaSimbolos[id.strip()] = Atributo(id.strip(),'')
				return Token(id.strip(),'ATRIBUTO',linhaGlobal,coluna)

def simuladorSintatico():
	global tabelaSimbolos
	while True:
		try:
			token = lex()
			for key, value in tabelaSimbolos.items():
				print(f"key {key} nome {value.nome} valor {value.valor}")
			print(f"<{token.tipo}, {token.atributo}, {token.linha}, {token.coluna}>")
			if token.tipo == 'Erro':
				break
		except EOFError:
			break
simuladorSintatico()
