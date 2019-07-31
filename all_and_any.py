from util import print_banner


def demo_all():
    if all(get_list()):
        print('All are true')
    else:
        print('Not all are true')

    if all([is_first_good(), is_second_good()]):
        print('All are goood')
    else:
        print('Not everyone good')

    if all(get_product_quality()):
        print('All products are good')
    else:
        print('Not all products are good')


def demo_any():
    if any(get_list()):
        print('Fond Truth')
    else:
        print('Did not found Truth')

    if any([is_first_good(), is_second_good()]):
        print('Found Good')
    else:
        print('None is good')

    if any(get_product_quality()):
        print('Found good product')
    else:
        print('No goood products found')


def get_list():
    return iter([True, True, True])


def is_first_good():
    return False


def is_second_good():
    return True


def get_product_quality():
    '''There is a reason behind third print line not reached at demo_all call
       There is a reason behind second and third print lines are not reached at demo_any call'''

    print('Reading first product quality')
    yield True
    print('Reading second product quality')
    yield False
    print('Reading third product quality')
    yield True


if __name__ == '__main__':
    print_banner('demo all')
    demo_all()
    print_banner('demo any')
    demo_any()
