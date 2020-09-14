import random
def draw_lake(num_fish = 20):
    counter = num_fish
    if counter >= 20:
        counter -= 20
        print("                                                                  ,  ,  ,                                 ")
        print("                                                               ,          ,                               ")
        print("                                                            ,               ,                             ")
        print("                                                         ,                    ,                           ")
        print("                                                      ,                         ,                         ")
        print("                                                   ,                              ,                       ")
        print("                                                 ,                 ><>              ,                     ")
        print("                                              ,          ~~~~~                        ,                   ")
        print("                                           ,                                           ,                  ")
        print("                                         ,          ><>                                 ,                 ")
        print("                                       ,                                       ><>       ,                ")
        print("                                      ,                                                   ,               ")
        print("                                      ,      ><>                            ~~~~~~        ,               ")
        print("                                       ,                                                 ,                ")
        print("                                        ,                                              ,                  ")
        print("                                         ,            ><>                            ,                    ")
        print("                                         ,                          ><>           ,                       ")
        print("                                       ,     ~~                                 ,                         ")
        print("                                    ,       ~~~~                              ,                           ")
        print("                                 ,                                            ,                           ")
        print("                               , ----OOO----OOO----OOO----OO----OOO----OOO----  ,                         ")
        print("                             ,                                      ><>           ,                       ")
        print("                           ,             ><>                                         ,                    ")
        print("                         ,                                ~~~                           ,                 ")
        print("                       ,           ><>                                                     ,              ")
        print("                     ,                                                  ><>                  ,            ")
        print("                   ,                       ~            ><>                                    ,          ")
        print("                 ,   ><>             ______0_____                                                ,        ")
        print("               ,                    | | |   \    \                                    ><>         ,       ")
        print("              ,                     | | |    \    \         \                                      ,      ")
        print("             ,                      | |_|    /    /          \   /~~~\             ><>              ,     ")
        print("            ,                       |_______/____/            \ /   . \                              ,    ")
        print("           ,                               0                  / \     /                               ,   ")
        print("          ,                                ~                 /   \___/                                 ,  ")
        print("          ,                                                 /                                          ,  ")
        while counter > 0:
            spaces = random.randint(1,90)
            print("          ," + " " * spaces + "><>" + " " * (89 - spaces) + ",  ")
            counter -= 1
        print("          ,                                                                                           ,   ")
        print("           ,---------------------+                                                                   ,    ")
        print("            ,| | | | | | | | | | |                                                                 ,      ")
        print("              ,| | | | | | | | | |                                                               ,        ")
        print("                ,| | | | | | | | |                                      ><>                   ,           ")
        print("                  ,--------------+                                                  ><>    ,              ")
        print("                    ,                 ><>                                              ,                  ")
        print("                      ,   ><>                                                       ,                     ")
        print("                        ,                                                        ,                        ")
        print("                          ,                ><>                                ,                           ")
        print("                             ,                                 ><>         ,                              ")
        print("                                 ,                                     ,                                  ")
        print("                                     ,                             ,                                      ")
        print("                                         ,                    ,                                           ")
        print("                                            ,    ,    ,   ,                                               ")
    else:
        to_remove = 20 - counter
        print("                                                                  ,  ,  ,                                 ")
        print("                                                               ,          ,                               ")
        print("                                                            ,               ,                             ")
        print("                                                         ,                    ,                           ")
        print("                                                      ,                         ,                         ")
        print("                                                   ,                              ,                       ")
        print("                                                 ,                                  ,                     ")
        to_remove -= 1
        print("                                              ,          ~~~~~                        ,                   ")
        print("                                           ,                                           ,                  ")
        if to_remove > 0:
            print("                                         ,                                              ,                 ")
            to_remove -= 1
        else:
            print("                                         ,          ><>                                 ,                 ")
        if to_remove > 0:
            print("                                       ,                                                 ,                ")
            to_remove -= 1
        else:
            print("                                       ,                                       ><>       ,                ")
        print("                                      ,                                                   ,               ")
        if to_remove > 0:
            print("                                      ,                                     ~~~~~~        ,               ")
            to_remove -= 1
        else:
            print("                                      ,      ><>                            ~~~~~~        ,               ")
        print("                                       ,                                                 ,                ")
        print("                                        ,                                              ,                  ")
        if to_remove > 0:
            print("                                         ,                                           ,                    ")
            to_remove -= 1
        else:
            print("                                         ,            ><>                            ,                    ")
        if to_remove > 0:
            print("                                         ,                                        ,                       ")
            to_remove -= 1
        else:
            print("                                         ,                          ><>           ,                       ")
        print("                                       ,     ~~                                 ,                         ")
        print("                                    ,       ~~~~                              ,                           ")
        print("                                 ,                                            ,                           ")
        print("                               , ----OOO----OOO----OOO----OO----OOO----OOO----  ,                         ")
        if to_remove > 0:
            print("                             ,                                                    ,                       ")
            to_remove -= 1            
        else:
            print("                             ,                                      ><>           ,                       ")
        if to_remove > 0:
            print("                           ,                                                         ,                    ")
            to_remove -= 1
        else:
            print("                           ,             ><>                                         ,                    ")
        print("                         ,                                ~~~                           ,                 ")
        if to_remove > 0:
            print("                       ,                                                                    ,             ")
            to_remove -= 1            
        else:
            print("                       ,           ><>                                                      ,             ")
        if to_remove > 0:
            print("                     ,                                                                         ,          ")
            to_remove -= 1            
        else:
            print("                     ,                                                  ><>                    ,          ")
        if to_remove > 0:
            print("                   ,                       ~                                                      ,       ")
            to_remove -= 1            
        else:
            print("                   ,                       ~            ><>                                       ,       ")
        if to_remove > 0:
            print("                 ,                   ______0_____                                                   ,     ")
            to_remove -= 1            
        else:
            print("                 ,   ><>             ______0_____                                                   ,     ")
        if to_remove > 0:
            print("               ,                    | | |   \    \                                                   ,    ")
            to_remove -= 1            
        else:
            print("               ,                    | | |   \    \                                    ><>            ,    ")
        print("              ,                     | | |    \    \         \                                        ,    ")
        if to_remove > 0:
            print("             ,                      | |_|    /    /          \   /~~~\                               ,    ")
            to_remove -= 1
        else:
            print("             ,                      | |_|    /    /          \   /~~~\             ><>               ,    ")
        print("            ,                       |_______/____/            \ /   . \                             ,     ")
        print("           ,---------------------+         0                  / \     /                            ,      ")
        print("            ,| | | | | | | | | | |         ~                 /   \___/                            ,       ")
        print("              ,| | | | | | | | | |                          /                                   ,         ")
        if to_remove > 0:
            print("                ,| | | | | | | | |                                                            ,           ")
            to_remove -= 1            
        else:
            print("                ,| | | | | | | | |                                      ><>                   ,           ")
        if to_remove > 0:
            print("                  ,--------------+                                                         ,              ")
            to_remove -= 1            
        else:
            print("                  ,--------------+                                                  ><>    ,              ")
        if to_remove > 0:
            print("                    ,                                                                  ,                  ")
            to_remove -= 1            
        else:
            print("                    ,                 ><>                                              ,                  ")
        if to_remove > 0:
            print("                      ,                                                             ,                     ")
            to_remove -= 1            
        else:
            print("                      ,   ><>                                                       ,                     ")
        print("                        ,                                                        ,                        ")
        if to_remove > 0:
            print("                          ,                                                   ,                           ")
            to_remove -= 1            
        else:
            print("                          ,                ><>                                ,                           ")
        if to_remove > 0:
            print("                             ,                                             ,                              ")
            to_remove -= 1            
        else:
            print("                             ,                                 ><>         ,                              ")
        print("                                 ,                                     ,                                  ")
        print("                                     ,                             ,                                      ")
        print("                                         ,                    ,                                           ")
        print("                                            ,    ,    ,   ,                                               ")
    return
