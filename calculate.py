import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {
		"perimeter-circle": 1,
		"area-circle": 1,
		"perimeter-square": 1,
		"area-square": 1,
}

def calc(fig, func, size):
		assert fig in figs, f"Figure {fig} is not supported. Available figures: {figs}"
		assert func in funcs, f"Function {func} is not supported. Available functions: {funcs}"

		result = eval(f'{fig}.{func}(*{size})')

		if func == 'perimeter':
				operation_str = f"Perimeter of {fig} ({' + '.join(map(str, size))}) = {result}"
		elif func == 'area':
				operation_str = f"Area of {fig} (π * {size[0]}^2) = {result}" if fig == 'circle' else f"Area of {fig} ({size[0]} * {size[0]}) = {result}"
		else:
				operation_str = f"{func} of {fig} with size {', '.join(map(str, size))} = {result}"

		return operation_str

if __name__ == "__main__":
		func = ''
		fig = ''
		size = []

		while fig not in figs:
				fig = input(f"Enter figure name, available are {figs}:\n")

		while func not in funcs:
				func = input(f"Enter function name, available are {funcs}:\n")

		while len(size) != sizes.get(f"{func}-{fig}", 1):
				size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

		operation_str = calc(fig, func, size)
		print(operation_str)
