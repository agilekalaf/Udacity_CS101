function GRAPHSEARCH (problem):
	frontier = {[initial]}; emplored = {}
	loop:
		if frontier is empty: return FAIL
		path = remove_choice(frontier)
		s = path.end; add s to explored
		if s is a goal: return path
		for a in actions:
			add [path + a->Result(s,a)]
			to frontier
			unless Result(s,a) in frontier + explored