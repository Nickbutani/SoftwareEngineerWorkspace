def flip_case(phrase, to_swap):
   return "".join([char.swapcase() if char.lower() in to_swap.lower() else char for char in phrase])
