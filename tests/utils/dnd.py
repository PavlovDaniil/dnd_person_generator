from bot.utils.dnd_get import get_classes

def test_get_calsses():
    assert get_classes() == ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

