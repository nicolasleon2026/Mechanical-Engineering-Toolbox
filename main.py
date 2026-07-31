from registry import CALCULATORS

def main():

    print("="*50)
    print("MECHANICAL ENGINEERING TOOLBOX")
    print("="*50)

    categories = list(CALCULATORS.keys())

    while True:

        print("\nCategories:")

        for i, cat in enumerate(categories, start=1):
            print(f"{i}. {cat}")

        print("0. Quit")

        choice = int(input("\nChoose category: "))

        if choice == 0:
            break

        category = categories[choice-1]

        calculators = CALCULATORS[category]

        print()

        for i, (name, _, _) in enumerate(calculators, start=1):
            print(f"{i}. {name}")

        calc_choice = int(input("\nChoose calculator: "))

        name, spec, fn = calculators[calc_choice-1]

        values = {}

        for key, label, kind, default in spec:

            if kind == "float":

                values[key] = float(
                    input(f"{label} [{default}]: ") or default
                )

            else:

                print(label)

                for i, option in enumerate(default, start=1):
                    print(i, option)

                selection = int(input("> "))

                values[key] = default[selection-1]

        result, fig = fn(values)

        print("\n-----------------------")
        print(result)
        print("-----------------------")

        if fig:
            fig.show()


if __name__ == "__main__":
    main()
