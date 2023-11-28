lista_de_alunos={}

while True:
    menu= int (input("""
                     1- Adicionar um novo aluno(a)
                     2- Remover um aluno(a)
                     3- Visualizar lista de alunos(as)
                     4- Sair 
                     """))
    
    if menu== 1:
         nome= str (input("Digite o nome do aluno(a): "))
         matricula= int (input("Digite a matricula do aluno: "))
         lista_de_alunos[matricula]= nome
         print(f"Aluno {nome} adicionado com sucesso com a matricula nº{matricula}!")


    elif menu == 2:
         matricula= int(input("Digite a matricula do aluno a ser removido: "))

         if matricula in lista_de_alunos:
             del lista_de_alunos[matricula]
             print (f"A matricula de nº {matricula}, foi removido(a)")
         else:
             print("Matriícula inexistente")    
         
    elif menu == 3:
         print ("Lista de todos os alunos:")
         for matricula, nome in lista_de_alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")

    elif menu == 4:
         print ("Saindo do Programa.")  
         break
    else:
         print("Opção inválida. Por favor, escolha uma opção válida")             
