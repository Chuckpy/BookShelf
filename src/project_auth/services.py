def password_check(passwd, list=None):
      
    SpecialSym =['!', '@', '#', '$', '%', '&', '*', '(', ')',
    '-', '+', '.', ',', ';', '?', '{', '[', '}', ']', '^', '>', '<', ':']
    val = True
    if list is None: list =[]

    if len(passwd) < 6:
        list.append('Comprimento deve ser, pelo menos 6')
        val = False
          
    if len(passwd) > 20:
        list.append('Comprimento não deve ser maior do que 8')
        val = False
          
    if not any(char.isdigit() for char in passwd):
        list.append('Senha deve ter pelo menos um numeral')
        val = False
          
    if not any(char.isupper() for char in passwd):
        list.append('Senha deve ter pelo menos uma letra maiúscula')
        val = False
          
    if not any(char.islower() for char in passwd):
        list.append('Senha deve ter pelo menos uma letra minúscula')
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        list.append('Senha deve ter pelo menos um dos símbolos : !@#$%&*()-+.,;?\{\[\}]^><:')
        val = False

    errors = list

    if val:
        return val, errors
