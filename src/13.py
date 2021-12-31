from aoc import main
from itertools import product

INPUT = "                      /---------------------\\           /----------------<---------------------------------------------------------------------\\      \n                      |                     |           |         /---------------------------\\                                                |      \n              /-------+---------------------+-----------+---------+---------------------------+------\\                                         |      \n   /----------+-------+---------------------+---\\      /+---------+---------------------------+------+------\\                                  |      \n /-+----------+-------+---------------------+---+------++---------+-------------------------\\ |      |      |                                  |      \n | |          |       |  /------------------+---+------++---------+-----\\                   | | /----+------+---------------------------\\      |      \n | |   /------+-------+--+------------------+---+-\\    ||         |     |              /----+-+-+----+------+----------------\\          |      |      \n | |   |      | /-----+--+------------------+---+-+----++---------+-----+--------------+----+-+-+----+---\\  |                |          |      |      \n | |   |      | |    /+--+--------------\\   |   | |    ||    /----+-----+--------------+----+-+-+----+---+--+----------------+---------\\|      |      \n | |   |      | |    ||  |              |   |   | |    ||    |    |     |              |    | | |    |   |  |                |         ||      |      \n | |   |      | |    ||  |      /-------+---+-\\ | |    ||    |    |     |              |    | | |    |   |  |        /-------+---------++------+---\\  \n | |   |      | |    ||  |      |       |   | | | |    ||    |    |     |     /--------+----+-+-+----+---+\\ |        |       |         ||      |   |  \n | |   |      | |    ||  |      |       |   | | | |    ||    |/---+-----+\\    |        |    | | |    |   || |        |       |         ||      |   |  \n | |   |    /-+-+----++--+------+-------+---+-+-+-+----++----++---+-----++--->+--------+----+-+-+----+---++-+-----\\  |       |         ||      |   |  \n | |   |    | | |   /++--+------+-------+---+-+-+-+----++----++---+-----++----+--------+----+-+-+----+---++-+-----+--+-------+-\\       ||      |   |  \n | |  /+----+-+-+---+++--+------+-------+---+-+-+-+----++-\\  ||   |     ||    |        |    | | |    |   || |     |  |       | |       ||      |   |  \n | |  ||    | | |   |||  |      |       |   | | | |    || | /++---+-----++----+--------+----+-+-+-\\  |   || |     |  |       | |       ||      |   |  \n | |  ||    |/+-+---+++--+------+-------+---+-+-+-+----++-+-+++---+\\  /-++----+--\\     |    | | | |  |   || |     |  |       | |/------++--\\   |   |  \n | |  ||    ||| |/--+++--+------+-------+---+-+-+-+----++\\| |||   ||  | ||    |  | /---+----+-+-+-+--+---++-+----\\|  |       | ||      ||  |   |   |  \n | |  ||    ||| ||  |||  |/-----+-------+---+-+-+-+----++++-+++---++--+-++----+--+-+---+----+-+-+-+--+---++-+----++--+-------+-++---\\  ||  |   |   |  \n | |  ||    ||| ||  |\\+--++-----+-------/   | | | |    |||| |||   v|  | ||    |  | |   |    | | | |  |/--++-+----++--+-------+-++---+--++--+---+--\\|  \n/+-+--++----+++-++--+-+--++-----+-----------+-+-+-+----++++-+++---++--+-++----+--+-+-\\ \\----+-+-+-+--++--++-+----++--+-------/ ||   |  ||  |   |  ||  \n|| | /++----+++-++--+-+--++-----+-----------+-+-+-+----++++-+++---++--+-++---\\|  | | |      | | | |  ||  || |    ||  |         ||   |  ||  |   |  ||  \n|| | |||    ||| ||  | |  ||     |           | | | |/---++++-+++---++--+-++---++--+-+-+------+-+-+-+--++--++-+----++--+---------++--\\|  ||  |   |  ||  \n|| | |||/---+++-++--+-+--++-----+-----------+-+-+-++---++++-+++---++--+-++---++--+-+-+---\\  | | | |  ||  || |    ||  |         ||  ||  ||  |   |  ||  \n|| | ||||   ||| ||  | |  ||     |           | | | ||   |||| |||   ||  | ||/--++--+-+-+---+--+-+\\| |  ||  || |    ||  |         ||  ||  ||  |   |  ||  \n|| | ||||   ||| || /+-+--++-----+-----------+-+-+-++---++++-+++---++--+-+++--++--+-+-+---+--+-+++-+--++--++-+----++--+-------\\ ||  ||  ||  |   |  ||  \n|| | ||||   ||| \\+-++-+--++-----+-----------+-+-+-++---++++-+++---++--+-+++--++--+-+-+---+--+-+++-+--++--/| |    ||  \\-------+-++--++--++--+---+--+/  \n|| | ||||   |||  |/++-+--++-----+-----------+-+-+-++---++++-+++---++--+-+++\\ ||  | | |   |  | ||| |  ||   | |    ||          | ||  ||  ||  |   |  |   \n|| | ||||   |||  |||| |  ||     |           | | | ||   |||| |||   ||  | |||| ||  | | |   |  | ||| |  ||   | |    ||          | ||  ||  ||  |   |  |   \n|| |/++++---+++--++++-+--++---\\ |           | | | ||   |||| |||   ||/-+-++++-++--+-+-+---+--+-+++-+--++---+-+----++----------+-++--++--++--+---+--+\\  \n|| ||||||   |||  |||| |  ||   | |           | | | ||   |||| |\\+---+++-+-++++-++--+-+-+---+--+-+++-+--++---+-+----++----------+-++--++--/|  |   |  ||  \n|| ||||||   |||  |||| |  ||   | |  /--------+-+-+-++---++++-+-+---+++-+-++++-++--+-+-+---+-\\| ||| |  ||   | |    ||          | ||  ||   |  |   |  ||  \n|| ||||||   |||  |||| | /++---+-+--+--------+-+-+-++---++++-+-+---+++-+-++++-++--+-+-+---+-++-+++-+--++-\\ | |    || /--------+-++--++---+--+\\  |  ||  \n|| ||||||   |||  |||| | |||   | |  |   /----+-+-+-++---++++-+-+---+++-+-++++-++--+-+-+---+-++-+++-+--++-+-+-+----++-+--------+-++--++---+--++--+-\\||  \n|| ||||||   |||  |||| | |||   | |  |   |    | | | ||  /++++-+-+--\\||| | |||| ||  |/+-+---+-++-+++-+--++-+-+-+----++-+--------+-++--++---+--++-\\| |||  \n|| ||||||   |||  |||| | |||  /+-+--+---+----+-+-+-++--+++++-+-+--++++-+-++++-++--+++-+---+-++-+++-+--++-+-+-+----++-+--\\     | ||  ||   |  || || |||  \n|| |||||| /-+++--++++-+-+++--++-+--+---+----+-+\\| ||  ||||| | |  |||| | |||| ||  ||| |   | || ||| |  || | | |    || |  |   /-+-++--++---+\\ || || |||  \n|| |||||| | |||  |||| \\-+++--++-+--+---+----/ ||| ||  ||||| | |  |||| | |||| ||  ||| |   | || ||| |  || | | |    || |  |   | | ||  ||   || || || |||  \n|| ||||\\+-+-+++--++++---+++--++-+--+---+>-----+++-/|  ||||| | |  |||\\-+-++++-++--+++-+---+-++-+++-+--++-+-+-+----++-+--+---+-+-++--++---++-++-++-++/  \n|| |||| | | |||  ||||   |||  || |  |   |/-----+++--+--+++++-+-+--+++--+-++++-++--+++-+---+-++-+++-+--++-+-+-+-\\  || |  |   | | ||  ||   || || || ||   \n|| |||| | | |||  |\\++---+++--++-+--+---++-----+++--+--+++++-+-+--+++--+-+++//++--+++-+---+-++-+++-+--++-+-+-+-+--++-+--+---+\\| ||  ||   || || || ||   \n|| |||| | | |||  | |\\---+++--++-+--+---++-----+++--+--+++++-+-+--+++--+>+++-+++--+++-+---+-++-+++-+--++-+-+-+-+--++-+--+---+++-/|  ||   || || || ||   \n|| |||| | | |||  | |    |||  || |  | /-++-----+++--+--+++++-+-+--+++--+-+++-+++--+++-+---+-++-+++-+--++-+-+-+-+--++-+--+---+++--+--++-<-++-++-++\\||   \n|| |||\\-+-+-+++--+-+----+++--++-+--+-+-++-----+++--+--++++/ | |  |||  | ||| |||  ||| |   | || ||| |  || |/+-+-+--++-+--+---+++--+--++---++-++-+++++\\  \n|| |||  | | |||  | |    |||  || |  | | ||     |||  |  ||||  \\-+--+++--+-+++-+++--+++-+---+-++-+++-/  || ||| | |  || |  |   |||  |  ||   || || ||||||  \n|| |||  | | |||  | |    |||  || |  | | ||/----+++--+--++++----+\\ |||  | ||| |||  |||/+---+-++-+++----++-+++-+-+--++-+--+---+++--+--++--\\|| || ||||||  \n|| |||  | | |||  | |    |||  || |  |/+-+++----+++--+--++++----++-+++--+-+++-+++--+++++---+-++-+++----++-+++-+-+--++-+--+---+++-\\|  ||  ||| || ||||||  \n|| \\++--+-+-+++--+-+----+++--++-+--+++-+++----++/  |  ||||    || |||  \\-+++-+++--/||||   | || |||    || ||| | |  || |  |   ||| ||  ||  ||| || ||||||  \n||  ||  | | |||  | |    |||  || |  ||| |||    ||   |  ||||    || |||    ||| ||\\---++++---+-++-+++----++-++/ | |  || |  |   ||| ||  ||  ||| || ||||||  \n||  ||  | | |||  | |    |||  || |  ||| |||    ||   |  ||||    \\+-+++----+/| \\+----++++---+-++-+++----++-++--+-+--++-+--+---+/| ||  ||  ||| || ||||||  \n||  || /+-+-+++--+-+----+++--++-+--+++-+++----++---+--++++-----+-+++----+-+--+----++++---+\\|| |||    || ||  | |  || \\--+---+-+-++--++--+++-+/ ||||||  \n||  || || | |||  | |   /+++--++-+--+++-+++----++---+--++++-----+-+++----+-+--+----++++---++++-+++----++-++--+-+--++--\\ |   | | ||  ||  ||| |  ||||||  \n||  || || | |||  | |   ||||  || |  ||| |||    ||   |  ||||     | |\\+----+-+--+----++++---++++-/||    || ||  | |  ||  | |   | | ||  ||  ||| |  ||||||  \n||  || || | |||  | |  /++++--++-+--+++-+++----++---+--++++-----+-+-+----+-+--+----++++---++++--++----++-++--+-+--++--+-+---+-+-++-\\||  ||| |  ||||||  \n||  || || | |||  | |  |||||  || |  ||| |||    ||   |  ||||     | | |    | |  |    ||||   |||| /++----++-++--+-+--++--+\\|   |/+-++-+++\\ ||| |  ||||||  \n||  || || | |||  | |  |||||  || |  ||| |||    ||   |/-++++-----+-+-+----+-+--+----++++---++++-+++\\   || ||  | |  ||  |||   ||| || |||| ||| |  ||||||  \n||  || || | |||  | | /+++++--++-+--+++<+++----++---++-++++-----+-+-+----+-+--+----++++---++++-++++---++-++--+\\|  ||  |||   ||| || |||| ||| |  ||||||  \n||  || || | |||  | | ||||||  || |  |\\+-+++----++---++-++++-----+-+-+----+-+--+----++++---++++-++++---++-++--+++--++--+++---+++-/| |||| ||| |  ||||||  \n||  || || | |||  | | |||\\++--++-+--+-+-+++----++---++-++++-----+-+-+----+-+--+----++++---++++-++++---++-/|  |||  ||  |||   |||  | |||| ||| |  |^||||  \n||  || || | |||  | |/+++-++--++-+--+-+-+++----++---++-++++-----+-+-+----+-+--+----++++\\  |||| ||||   |\\--+--+++--++--+++---+++--+-++++-+++-+--++++/|  \n||  || || | |||  | ||||| ||  || |  | | |||    ||   || ||||     | | |    | |  |    ||\\++--++++-++++---+---+--+++--++--+++---+++--+-++++-/|| |  |||| |  \n||  || || | |||  | ||||| ||  || |  | | |||    ||   || ||||     | | |    | |  |    || ||  |||| ||||   |   |  |||  ||  |||   |||  | ||||  || |  |||| |  \n||  || || | \\++--+-+++++-++--++-+--+-+-+++----++---++-++++-----+-+-+----+-+--+----++-++--++++-++++---+---+--+++--+/  |||   |||  | ||||  || |  |||| |  \n||  || || |  ||  | ||||| ||  || |  | | |||    ||   || ||||     | | |    | |  |    || ||  |||| ||||   |   |  |||  |   |||   |||  | ||||  || |  |||| |  \n||  ||/++-+--++--+-+++++-++--++-+--+-+-+++----++---++-++++-----+-+-+----+-+--+----++-++\\ |||| ||||   |   |  |||  |   |||   |||  | ||||  || |  |||| |  \n||  \\++++-+--++--+-+++++-++--+/ |  | | ||| /--++---++-++++-----+-+-+----+-+--+----++-+++-++++-++++>--+---+--+++--+---+++---+++--+\\||||  || |  |||| |  \n||   |||| |  ||  | ||||| |\\--+--+--+-+-+++-+--++---++-++++-----+-+-+----+-+--+----++-+++-++++-++++---+---+--+++--+---+++---+++--++++/|  || |  |||| |  \n||   |||| |  ||  | ||||| |   |  |  | | ||\\-+--++---++-++++-----/ | |    |/+--+----++-+++\\|||| ||||   |/--+--+++--+---+++---+++--++++-+--++-+-\\|||| |  \n||   |||| |  ||  | ||||| |   |  |  | | ||  |/-++---++-++++-------+-+----+++--+----++-++++++++-++++---++--+--+++--+---+++---+++--++++-+--++\\| ||||| |  \n||   |||| |  ||  | ||||| | /-+--+--+-+-++--++-++---++-++++-------+-+----+++--+----++-++++++++-++++---++--+--+++\\ |   |||   |||  |||| |  |||| ||||| |  \n|\\---++++-+--++--+-+++++-+-+-+--+--+-+-++--++-++---++-++++-------+-+----+++--+----++-+++++++/ ||||   ||  |  |||| |   |||   |||  |||| |  |||| ||||| |  \n|    |||\\-+--++--+-+++++-+-+-+--+--+-+-++--++-++---++-++++-------+-+----+++--+----++-++++/||  ||||   ||  |  |||| |   |||   |||  |||| |  |||| ||||| |  \n|    |||/-+--++--+-+++++-+-+-+--+--+-+-++--++-++---++-++++-------+-+-\\  |||  |    || |||| ||  ||||   ||  |  |||| |   |||   |||  |||| |  |||| ||||| |  \n|    |||| |  ||  | ||||| | | |  |  | | ||  || ||   |\\-++++-------+-+-+--+++--+----++-++++-++--+++/   ||  |  |||| |   |||   |||  \\+++-+--+++/ ||||| |  \n|    |||| |  ||  | ||||| | | |/-+--+-+-++--++-++---+--++++-------+-+-+--+++--+----++-++++-++--+++----++--+--++++\\|   |||   |||   ||| |  |||  ||||| |  \n|    |||| |  ||  | ||||| | | || |  | | ||  || || /-+--++++-------+-+-+--+++--+--\\ || |||| ||  |||    ||  |  ||||||   |||   |||   ||| |  |||  ||||| |  \n|    |||| |  ||  | ||||| \\-+-++-+--+-+-++--++-++-+-+--++++-------+-+-+--/||  |  | || |||| ||  |||    ||  |  ||||||   |||   |||   ||| |  |||  ||||| |  \n|    |||| |  ||  | |||||   | || |  | | ||  || || | |  |||| /-----+-+-+---++--+--+-++-++++-++--+++----++--+--++++++---+++---+++\\  ||| |  |||  ||||| |  \n|    |||| |  \\+--+-+++++---+-++-+--+-+-++--++-++-+-+--++++-+-----+-/ |   ||  |  | || |||| ||  |||   /++--+--++++++\\  |||   |||| /+++-+--+++\\ ||||| |  \n|    |||| \\---+--+-+++++---+-++-+--+-+-++--++-+/ v |  |\\++-+-----+---+---++--+--+-++-++++-++--+++---+++--+--/||||||  |||   |||| |||| |  |||| ||||| |  \n|    ||||  /--+--+-+++++--\\|/++-+--+-+-++--++-+--+-+--+-++-+-----+---+---++--+--+-++-++++-++--+++---+++--+\\  ||||||  |||   |||| |||| |  |||| ||||| |  \n|    ||||  |  | /+-+++++--+++++-+--+-+-++--++-+--+-+--+-++-+-----+---+---++-\\|  | || |||| ||  |||   |||/-++--++++++-\\|||   |||| |||| |  |||| ||||| |  \n|    ||||  |  | || |||||  ||||| |  | | ||  || |  | |  | || |/----+---+---++-++--+-++-++++-++--+++---++++-++--++++++-++++\\  |||| |||| |  |||| ||||| |  \n\\----++++--+--+-++-+++++--+++++-+--+-+-++--++-+--+-+--+-++-++----+---+---++-++--+-++-/||| ||  |||   |||| ||  |||||| |||||  |||| |||| |  |||| ||||| |  \n    /++++--+--+-++-+++++\\ |||\\+-+--+-+-++--++-+--+-+--+-++-++----+---+---++-++--+-++--+++-++--+++---++++-++--++++++-+++/|  |||| |||| |  |||| ||||| |  \n    |||||/-+--+-++-++++++-+++-+-+-\\| \\-++--++-+--+-+--+-++-++----+---+---++-++--+-++--+++-++--+++---++++-++--++++++-+++-+--++++-++++-+--++++-+++/| |  \n    |||||| |  | || |||||| |\\+-+<+-++---++--++-+--+-+--+-++-++----+---+---++-++--+-++--+++-++--+++---++++-++--++/||| ||| |  |||| |||| |  |||| ||| | |  \n    |||||| |  | || |||||| | | \\-+-++---++--++-+--+-+--+-++-++----+---+---++-++--+-++--+++-++--+++---++++-++--++-/|| ||| |  |||| |||| |  |||| ||| | |  \n    |||||| |  | || |||||| | |   | ||   ||  || |  \\-+--+-++-++----+---+---++-++--/ ||  ||| ||  |||   |||| ||  ||  || ||| |  |||| |||| |  |||| ||| | |  \n    |||||| |  | || |||\\++-+-+---+-++---++--++-+----+--+-++-++----+---+---++-++----++--+++-++--+++---++++-++--++--++-+++-+--++++-++/| |  |||| ||| | |  \n    |||||| |  |/++-+++-++-+-+---+-++---++--++-+----+--+-++-++----+---+---++-++----++--+++-++\\ |||   |||| ||  ||  || ||| |  |||| || | |  |||| ||| | |  \n    |||||| |  |||| ||| || | |   | |\\---++--++-+----+--+-++-++----+---+---++-++----++--+++-+/| |||   |||| ||  ||  || ||| |  |||| || | |  |||| ||| | |  \n    |||||| |  |||| ||| || | |   | |    ||  \\+-+----+--+-++-++----+---+---++-++----++--+++-+-+-+++---++++-++--++--++-+++-+--++++-+/ | |  |||| ||| | |  \n    |||||| |  |||| ||| || | |   | |    ||/--+-+----+--+-++-++---\\|   |   || ||    ||  ||| | | |||   |||| ||  ||  || ||| |  |||| |  | |  |||| ||| | |  \n    |||||| |  |||| ||| || | |   | |    |||  | |    |  | || ||   ||   |   || ||    ||  ||| | | ||\\---++++-++--++--++-+++-+--++++-+--+-+--/||| ||| | |  \n    |||||| |  |||| ||| |^ | |   | |    |||  | |    |  | || ||   ||   |   || ||    ||  |||/+-+-++----++++-++--++--++-+++\\|  |||| |  | |   ||| ||| | |  \n  /-++++++-+--++++\\||| || | |   | |    |||  | |    |  | || ||   ||   |   \\+-++----++-<++/|| | ||    |||| ||  ||  || |||||  |||| |  | |   ||| ||| | |  \n  | |||||| \\--++++++++-++-/ |   | |    ||| /+-+----+--+-++-++---++---+---\\| || /--++--++-++-+-++----++++-++--++--++-+++++--++++-+--+\\|   ||| ||| | |  \n  | ||||||    |||||||| ||   |   | |    ||| || |    |  | || ||   ||   |   || || |  ||  || || | \\+----++++-++--++--++-++/||  |||| |  |||   ||| ||| | |  \n  | ||||||    |||||||| ||   |   | | /--+++-++-+----+--+-++-++---++---+\\  || || |  \\+--++-++-+--+----++++-++--++--++-++-++--++++-+--+++---+++-+/| | |  \n  | ||||||    |||||||| ||   |   | | |  ||| || |    | /+-++-++---++---++--++-++-+---+--++-++-+--+----++++-++--++--++-++-++--++++-+--+++---+++-+-+-+-+\\ \n  | ||||||    |||||||| ||   |   | | |  ||| || |    | || \\+-++---++---++--++-++-+---+--++-++-+--+----++++-++--++--++-++-++--++++-+--+++---+++-+-/ | || \n  | ||||||    \\+++++++-++---+---+-+-+--+++-++-+----+-++--+-++---++---++--++-++-+---+--++-++-+--+----+/|| ||  ||  || || ||  |||| |  |||   ||| |   | || \n  | ||||||     ||||||| ||   |   | | |  ||| || |    | ||  | ||   ||   ||  || || |   |  || || |  |    | || ||  ||  || || ||  |||| |  |||   ||| |   | || \n  | ||||||     ||||||| ||   |   | | |  \\++-++-+----+-++--+-++---++---++--++-++-+---+--++-++-+--+----+-++-++--++--++-++-++--++++-+--+++---+++-+---/ || \n  | \\+++++-----+++++++-+/   |   \\-+-+---++-++-/    | ||  | ||   ||   ||  || || |   \\--++-++-+--+----+-++-++--++--/| || ||  |\\++-+--++/   ||| |     || \n  |  |v|||/----+++++++-+----+--\\  | |   || ||      \\-++--+-++---++---++--++-++-+------++-++-+--+----+-++-++--++---+-++-++--+-++-+--/|    ||| |     || \n  |  ||||||    \\++++++-+----+--+--+-+---++-++--------++--+-++---++---++--++-++-+------++-++-/  |    | || ||  ||   | || ||  | || |   |    ||| |     || \n  |  ||||||   /-++++++-+----+--+--+-+---++-++--------++--+-++---++---++--++-++-+------++-++----+----+-++\\||  ||   | || ||  | || |   |    ||| |     || \n  |  ||||||   | |||||| |    |  |  | |   \\+-++--------++--+-++---++---++--++-++-+------++-++----+----+-+++++--+/   | || ||  | || |   |    ||| |     || \n  |  ||||||   | |||||| \\----+--+--+-+----+-++--------++--+-++---++---++--++-++-+------++-++----+----+-+++++--+----+-+/ ||  | || |   |    ||| |     || \n  \\--++++++---+-++/|||      |  |  | |    | ||        ||  | ||   ||   ||  || || |   /--++-++----+----+-+++++--+----+-+--++\\ | || |   |    ||| |     || \n     ||||||   | || |||      |  |  | |    | \\+--------++--+-++---++---++--/| || |   |  || ||    |    | |||||  |    | |  ||| | || |   |    ||| |     || \n     \\+++++---+-++-+++------+--+--+-+----+--+--------++--+-++---++---++---+-+/ \\---+--++-++----+----+-+++++--+----+-+--+++-+-++-+---/    ||| |     || \n      ||||| /-+-++-+++------+--+--+-+----+--+--------++--+-++---++---++---+-+------+--++-++----+----+-+++++--+\\   | |  ||| \\-++-+--------/|| |     || \n      ||||| | | || |||      \\--+--+-+----+--+--------++--+-++---++---++---+-+->----+--++-++----+----+-++++/  ||   | |  |||   || |         || |     || \n      ||||| | | || |||         |  | |    |  |        |\\--+-++---+/   ||/--+-+------+--++-++----+---\\| |\\++---++---+-/  |||   || |         || |     || \n /----+++++-+-+-++\\|||         |  | |    \\--+--------+---+-++---/    |||  | |      |  || ||    |   || | |\\---++---+----+++---++-+---------++-+-----/| \n |    ||||| | | ||||||         |  | |       |        |   | ||        |||  | |      |  || ||    |   || | |    ||   |    |||   || |         || |      | \n |    ||||| | | |\\++++---------+--+-+-------+--------+---/ ||        |||  | |      |  || ||    |   || | |    ||   |    |||   || |         || |      | \n |    ||||| | | | ||||         |  | |       |        |     ||   /----+++--+-+------+--++-++----+---++-+-+----++---+----+++---++-+------\\  || |      | \n |    ||||| | | | ||||         |  | |       |        \\-----++---+----+++--+-+------+--++-++----+---++-+-+----++---+----+++---++-+------+--++-+------/ \n |    ||||| | | | ||||         |  | \\-------+--------------++---+----+/|  | |      |  || ||    |   || | |    ||   |    ||| /-++-+------+-\\|| |        \n |    ||||| | | | ||||         |  |         |              \\+---+----+-+--+-+------+--++-++----+---++-+-+----++---+----+++-+-+/ |      | ||| |        \n |    ||||| | \\-+-++++---------+--+---------+---------------+---+----+-+--+-+------+--++-++----+---++-+-/    ||   |    ||| | |  |      | ||| |        \n |    ||||| |   | |||\\---------+--+---------+---------------+---+----+-+--+-+------+--++-++----+---++-+------/|   |    ||| | |  |      | ||| |        \n |/---+++++-+---+-+++-\\        |  |     /---+---------------+---+----+-+--+-+------+--++-++----+---++-+-------+---+----+++-+-+--+------+\\||| |        \n \\+---+++++-+---+-/|| |        |  |     |   |               |/--+----+-+--+-+------+--++-++----+---++-+-----\\ |   |    ||| | |  |      ||||| |        \n  |   \\++++-+---+--++-+--------+--+-----+---+---------------++--+----+-+--+-+------+--+/ ||    |   || |     | |   |    ||| | |  \\------++++/ |        \n  |    |||| |   |  || |        |  |     |   |               ||  |    | |  \\-+------+--+--++----/   || |     | |   |    ||| | |         ||||  |        \n  |    |||| |   |  || |        |  |     v   |               ||  |    | |    |      |  |  \\+--------++-+-----+-+---+----/|| | |         ||||  |        \n  |    ||\\+-+---+--++-+--------+--/     |   |               ||  |    | |    |      |  |   |        |\\-+-----+-+---/     || | |         ||||  |        \n  |    || | |   |  \\+-+--------+--------+---+---------------++--+----+-+----+------+--+---+--------+--+----<+-+---------++-+-/         ||||  |        \n  |    || | |   |   \\-+--------+--------+---+---------------++--+----+-+----+------+--/   |        |  |     | |         || \\-----------++/|  |        \n  |    \\+-+-+---+-----+--------+--------+---+---------------++--+----+-+----+------+------/        |  |     | |         ||             || |  |        \n  |     | | |   |     |        |        \\---+---------------++--+----+-+----+------+---------------+--+-----+-+---------++-------------+/ |  |        \n  |     | | |   |     |        |            |               ||  |    | |    |      |               |  |     | |         ||             |  |  |        \n  |     | | \\---+-----+--------+------------+---------------++--+----+-+----+------+---------------+--+-----+-/         ||             |  |  |        \n  |     | |     \\-----+--------+------------+---------------++--+----+-+----/      |               |  |     |           ||             |  |  |        \n  |     | |           |        |            |    /----------++--+----+-+-----------+---------------+--+-----+-----------++----\\        |  |  |        \n  |     | |           |        |            |    |          \\+--+----+-+-----------+---------------+--+-----+-----------/|    |        |  |  |        \n  \\-----+-+-----------/        |            |    |           \\--+----+-+-----------+---------------+--+-----/            |    |        |  |  |        \n        | |                    |            \\----+--------------+----+-+-----------+---------------+--+------------------+----+--------+--/  |        \n        | |                    |                 |              |    | |           \\---------------+--+------------------/    |        |     |        \n        \\-+--------------------+-----------------+--------------+----/ |                           |  |                       |        |     |        \n          |                    |                 |              |      \\---------------------------/  |                       |        |     |        \n          \\--------------------/                 |              \\-------------------------------------+-----------------------+--------/     |        \n                                                 |                                                    \\-----------------------+--------------/        \n                                                 \\----------------------------------------------------------------------------/                       "
DR, DC = [0,1,0,-1], [1,0,-1,0]

def move_cart(crosses: dict[tuple[int,int],str], cart: list[int]) -> list[int]:
  r,c,d,t = cart
  match crosses.get((r,c), " ")[0]:
    case '+':
      match t:
        case 0: d = [3,0,1,2][d]
        case 2: d = [1,2,3,0][d]
      t = (t+1)%3
    case '/':  d = [3,2,1,0][d]
    case '\\': d = [1,0,3,2][d]
  return [r+DR[d],c+DC[d],d,t]

def step(crosses: dict[tuple[int,int],str], carts: list[list[int]]) -> set[int]:
  carts.sort()
  crashes = set()
  for i in range(len(carts)):
    r,c,d,t = move_cart(crosses, carts[i])
    for j in range(len(carts)):
      if carts[j][0] == r and carts[j][1] == c:
        crashes.add(i)
        crashes.add(j)
    carts[i] = [r,c,d,t]
  return crashes

def part1(crosses: dict[tuple[int,int],str], carts: list[list[int]]):
  while True:
    crashes = step(crosses, carts)
    if crashes:
      break
  r,c = carts[crashes.pop()][:2]
  return f"{c},{r}"

def part2(crosses: dict[tuple[int,int],str], carts: list[list[int]]):
  while len(carts) > 1:
    for i in reversed(sorted(step(crosses, carts))):
      carts.pop(i)
  r,c = carts[0][:2]
  return f"{c},{r}"

def solve():
  grid = [list(s) for s in INPUT.split('\n')]
  crosses, carts = {}, []
  for r,c in product(range(len(grid)), range(len(grid[0]))):
    match grid[r][c]:
      case '>': carts.append([r,c,0,0])
      case 'v': carts.append([r,c,1,0])
      case '<': carts.append([r,c,2,0])
      case '^': carts.append([r,c,3,0])
      case '+': crosses[r,c] = '+',
      case '/': crosses[r,c] = '/',
      case '\\': crosses[r,c] = '\\',
  return part1(crosses, carts[:]), part2(crosses, carts[:])

main(solve)
