def cal_fuel(mw):
    return (mw //3) - 2

if __name__ == "__main__":
    with open('data/d01.data') as fp:
        data = fp.readlines()

    modules = ([ int(x.rstrip()) for x in data])
    
    ans_1 = sum(cal_fuel(m) for m in modules)
    print(ans_1)

    total_fuel_req = list()

    for module in modules:
        module_fuel_req = list()
        while cal_fuel(module) > 0:
            fr = cal_fuel(module)
            module_fuel_req.append(fr)
            module = fr
        total_fuel_req.append(sum(module_fuel_req))
    
    print("Total fuel requirements", sum(total_fuel_req))        