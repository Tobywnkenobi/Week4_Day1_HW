import random

def create_show(fireworks, show_time):
    fireworks.sort()

    show = []                                   #this is a constant O(1)

    remaining_time = show_time                      #O(1)


    while remaining_time > 0 and fireworks:     #O(n)

           # Select a random firework

           firework = random.choice(fireworks)      #O(1)


           if firework <= remaining_time:               #O(n)

               # Add the firework to the show

               show.append(firework)                    #O(1)

               remaining_time -= firework               #overall O(n2))

           else:

              # This firework is too long, remove it from consideration

              fireworks.remove(firework)

    return show