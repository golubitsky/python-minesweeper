import re

def determine_operation(retry_reason):
    if retry_reason:
        r = {'fail': general_fail, 'help': print_help}
        r[retry_reason]()
        
    x = y = 0
    captured = input('Type command or (h)elp:')
    if re.search('h', captured):
        return {'retry_user_input': 'help'}

    coords = re.findall('\d+', captured)
    if coords and len(coords) == 2:
        x, y = map(int, coords)

    flag_mine = re.search('f', captured)
    reveal_cell = re.search('r', captured)
    
    if flag_mine and x and y:
        return {operation: 'flag', x: x, y: y}
    elif reveal_cell and x and y:
        print(f'Going to reveal {x}, {y}')
    else:
        return {'retry_user_input': 'fail'}

    
def general_fail():
    print("Invalid input, try again or use 'h' for help")
    
def print_help():
    print('Specify x and y coordinates (in x,y order) to execute operation on.')
    print('Acceptable operations are f (flag) and r (reveal).')
    print("Acceptable input: '3,1,f' or '2 4 r' or 'r 2 4'")
    print('Visit https://en.wikipedia.org/wiki/Minesweeper_(video_game) for additional info.')