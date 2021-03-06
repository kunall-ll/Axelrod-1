"""Stochastic variants of Lookup table based-strategies, trained with particle
swarm algorithms.

For the original see:
 https://gist.github.com/GDKO/60c3d0fd423598f3c4e4
"""

from axelrod.actions import Actions, Action
from axelrod.load_data_ import load_pso_tables
from axelrod.player import Player
from axelrod.random_ import random_choice
from .lookerup import LookerUp, create_lookup_table_from_pattern


C, D = Actions.C, Actions.D
tables = load_pso_tables("pso_gambler.csv", directory="data")


class Gambler(LookerUp):
    """
    A stochastic version of LookerUp which will select randomly an action in
    some cases.
    """

    name = 'Gambler'
    classifier = {
        'memory_depth': float('inf'),
        'stochastic': True,
        'makes_use_of': set(),
        'long_run_time': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def strategy(self, opponent: Player) -> Action:
        action = LookerUp.strategy(self, opponent)
        # action could be 'C', 'D', or a float
        if action in [C, D]:
            return action
        return random_choice(action)


class PSOGamblerMem1(Gambler):
    """
    A 1x1x0 PSOGambler trained with pyswarm. This is the 'optimal' memory one
    strategy trained against the set of short run time strategies in the
    Axelrod library.

    Names:
        - PSO Gambler Mem1: Original name by Marc Harper
    """

    name = "PSO Gambler Mem1"

    def __init__(self) -> None:
        pattern = tables[("PSO Gambler Mem1", 1, 1, 0)]
        lookup_table = create_lookup_table_from_pattern(
            plays=1, op_plays=1, op_start_plays=0,
            pattern=pattern)
        super().__init__(lookup_table=lookup_table)
        self.classifier['memory_depth'] = 1


class PSOGambler1_1_1(Gambler):
    """
    A 1x1x1 PSOGambler trained with pyswarm.

    Names:
        - PSO Gambler 1_1_1: Original name by Marc Harper
    """

    name = "PSO Gambler 1_1_1"

    def __init__(self) -> None:
        pattern = tables[("PSO Gambler 1_1_1", 1, 1, 1)]
        lookup_table = create_lookup_table_from_pattern(
            plays=1, op_plays=1, op_start_plays=1,
            pattern=pattern)
        super().__init__(lookup_table=lookup_table)


class PSOGambler2_2_2(Gambler):
    """
    A 2x2x2 PSOGambler trained with pyswarm. Original version by @GDKO.

    Names:
        - PSO Gambler 2_2_2: Original name by Marc Harper
    """

    name = "PSO Gambler 2_2_2"

    def __init__(self) -> None:
        pattern = tables[("PSO Gambler 2_2_2", 2, 2, 2)]
        lookup_table = create_lookup_table_from_pattern(
            plays=2, op_plays=2, op_start_plays=2,
            pattern=pattern)
        super().__init__(lookup_table=lookup_table)


class PSOGambler2_2_2_Noise05(Gambler):
    """
    A 2x2x2 PSOGambler trained with pyswarm with noise=0.05.

    Names:
        - PSO Gambler 2_2_2 Noise 05: Original name by Marc Harper

    """

    name = "PSO Gambler 2_2_2 Noise 05"

    def __init__(self) -> None:
        pattern = tables[("PSO Gambler 2_2_2 Noise 05", 2, 2, 2)]
        lookup_table = create_lookup_table_from_pattern(
            plays=2, op_plays=2, op_start_plays=2,
            pattern=pattern)
        super().__init__(lookup_table=lookup_table)
