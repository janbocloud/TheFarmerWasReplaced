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
class Entities:
	Hay = 0
	Bush = 1

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
	畑の最大サイズを返します。
	"""
	return 0

#####################
# Game Settings END #
#####################


def main():
	# 無限ループ
	while True:

		# 3回繰り返す
		for i in range(3):
			# 条件分岐
			if can_harvest():
				# 収穫できる場合
				harvest()
				# Bushを植える
				plant(Entities.Bush)

			# 北に移動する
			move(North)

		# 東に移動する
		move(East)
