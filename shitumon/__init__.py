from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire' #URLに表示される名前 (好きに決めてい 
    PLAYERS_PER_GROUP = None #何人グループで行うアプリか。質問紙 
    NUM_ROUNDS = 1 #何ラウンド繰り返すか。質問紙なので1でよい 


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q_gender = models. CharField(initial = None,
                                    choices = ['男性', '女性', '回答しない'],
                                    verbose_name = 'あなたの性別を教えてください',
                                    widget = widgets.RadioSelect)

    q_age = models.IntegerField(initial = None,
                                    verbose_name = 'あなたの年齢を教えてください',
                                    choices = range(0, 125)
                                    )
    
    q_area = models.CharField(initial = None,
                                choices = ['北海道', '東北地方', '関東地方', '中部地方', '近畿地方', '中国地方', '四国地方', '九州地方'],
                                verbose_name = 'あなたのお住まいの地域を教えてください'
                                )
    q_tanmatsu = models.CharField(initial = None,
                                    choices = ['パソコン', 'タブレット', 'スマートフォン', 'それ以外'],
                                    verbose_name = '解答端末を教えてください',
                                    widget = widgets.RadioSelect
                                    )
    q_hitorigurashi = models.CharField(initial = None,
                                        choices = ['はい', 'いいえ'],
                                        verbose_name = 'あなたは一人暮らしですか',
                                        widget = widgets.RadioSelect
                                        )
    q_student = models.BooleanField(initial = None,
                                    choices = [(True, 'はい'), (False, 'いいえ')],
                                    verbose_name = 'あなたは学生ですか',
                                    widget = widgets.RadioSelect
                                    )


# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = [
        'q_gender', 'q_age', 'q_area', 'q_tanmatsu', 'q_hitorigurashi', 'q_student'
        ]

class Page2(Page): pass

page_sequence = [Page1, Page2]
