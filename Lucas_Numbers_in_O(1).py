def Craby_patty_secret_formula(n):
    invroot5 = 1/m.sqrt(5)
    ax1 = ((1+m.sqrt(5))/2)**n
    ax2 = ((1-m.sqrt(5))/2)**n
    return int(invroot5*(ax1-ax2))
  
  
  def Lucas_number(n):
    return (Craby_patty_secret_formula(n-1)+Craby_patty_secret_formula(n+1))
