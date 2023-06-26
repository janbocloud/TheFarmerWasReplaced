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

#####################
# Game Settings END #
#####################


# Answer
def main():
	pass

