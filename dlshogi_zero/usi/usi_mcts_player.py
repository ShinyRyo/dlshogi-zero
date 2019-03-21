﻿from dlshogi_zero.usi.usi import *
from dlshogi_zero.player.mcts_player import MCTSPlayer

def run():
    player = MCTSPlayer(64)
    usi(player)

if __name__ == '__main__':
    run()