from otree.api import *


doc = "はじめての独裁者ゲーム"


class C(BaseConstants):
    NAME_IN_URL = 'dictator_trial'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 5
    ENDOWMENT = cu(10)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    proposal = models.CharField(
        choices = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        label = 'プレイヤー2にいくら渡しますか?',
        widget = widgets.RadioSelect
    )


class Player(BasePlayer):
    pass

def compute(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_plater_by_id(2)
    p1.payoff = C.ENDOWMENT - group.proposal
    p2.payoff = group.proposal

def creating_session(subsession: Subsession):
    subsession.group_randomly()


# PAGES
class Page1(Page):
    pass

class Page2(Page):
    form_model = 'group'
    form_fields = ['proposal']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1


class Page3(WaitPage):
    after_all_player_arrive = compute


class Page4(Page):
    pass


page_sequence = [Page1, Page2, Page3, Page4]
