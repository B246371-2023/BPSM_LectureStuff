def history(howmany=20) :
  import readline
  his_start = readline.get_current_history_length()-howmany
  his_stop = readline.get_current_history_length()
  for this in range(his_start,his_stop) :
    print(readline.get_history_item((this + 1)),"#",this)
   
