# NOTE #
"""
Visual Studio Codeを使用している場合、次のショートカットで全てのコードの折り畳みや展開をすることができるため、コードが見やすくなるかもしれません。
全て折り畳む：「Ctrl + K」「Ctrl + 0」
全て展開：「Ctrl + K」「Ctrl + J」
"""

#################
# Game Settings #
#################

# Constant
North = 0
West = 1
East = 2
South = 3

# Class
class Items:
	Hay = 0
	Wood = 1
	Carrot = 2
	Carrot_Seed = 3

class Entities:
	Hay = 0
	Bush = 1
	Carrots = 2
	Tree = 3

class Grounds:
	Soil = 0
	Turf = 1

# Function
def harvest():
	"""
	作物の収穫を行います。
	"""
	pass
def move(direction):
	"""
	ドローンを指定方向へ移動します。

	Parameters
	----------
	direction : int
		方角
	"""
	pass
def plant(entities):
	"""
	指定した作物を植えます。

	Parameters
	----------
	entities : Entities
		作物の種類
	"""
	pass
def can_harvest():
	"""
	作物を収穫できるか判定した結果を返します。
	"""
	return True
def do_a_flip():
	"""
	ドローンが宙返りをします。
	"""
	pass
def get_world_size():
	"""
	畑の大きさを返却します。
	"""
	return 0
def get_pos_x():
	"""
	ドローンの位置(X座標)を返却します。
	"""
	return 0
def get_pos_y():
	"""
	ドローンの位置(Y座標)を返却します。
	"""
	return 0
def num_items(items):
	"""
	アイテムの所持数を返却します。

	Parameters
	----------
	items : Items
		アイテム
	"""
	return 0
def get_time():
	"""
	ゲーム開始時からの経過時間を表示します。
	"""
	return 0
def get_entity_type():
	"""
	ドローン下の作物を返却します。
	"""
	return Entities.Bush
def get_ground_type():
	"""
	ドローン下の畑の状態を返却します。
	"""
	return Grounds.Turf
def quick_print(str):
	"""
	コンソールにのみ出力します。
	"""
	print(str)
def till():
	"""
	畑の状態を変化させます。
	"""
	pass
def trade(items):
	"""
	アイテムに交換して取得します。

	Parameters
	----------
	items : Items
		交換するアイテム
	"""
	pass

#####################
# Game Settings END #
#####################


# Answer
def main():
	pass

