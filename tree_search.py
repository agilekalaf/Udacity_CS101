function TREESEARCH (problem):
	frontier = {[initial]}
	loop:
		if frontier is empty: return FAIL
		path = remove_choice(frontier)
		s = path.end
		if s is a goal: return path
		for a in actions:
			add [path + a->Result(s,a)]
			to frontier