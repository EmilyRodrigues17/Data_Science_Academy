#!/usr/bin/env python
# coding: utf-8

# ## CALCULADORA

# In[8]:


print('*********************************** Python Calculator ********************************************')


# ## Funções

# In[9]:


def soma(n1, n2):
    return n1 + n2


# In[10]:


def subtracao(n1, n2):
    return n1 - n2


# In[11]:


def multiplicacao(n1, n2):
    return n1 * n2


# In[12]:


def divisao(n1, n2):
    return n1/n2


# ## Calculadora

# In[13]:


print('Selecione o número da operação desejada:')

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

opcao = int(input('Digite sua opção (1/2/3/4): '))


# In[14]:


cont = 0
while cont != 1:
    if (opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4):
        print('Opção invalida!')
        print('Digite novamente')
        opcao = int(input('Digite sua opção (1/2/3/4): '))
        
    else:            
        print('entrou')
        cont = cont + 1
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número:'))
        
        if (opcao == 1):
            print('A soma é: ', soma(n1,n2))
        if (opcao == 2):
            print('A subtração é: ', subtracao(n1,n2))
        if (opcao == 3):
            print('A multiplicação é: ', multiplicacao(n1,n2))
        if (opcao == 4):
            print('A divisão é: ', divisao(n1,n2))
        
        


# In[ ]:





# In[ ]:




