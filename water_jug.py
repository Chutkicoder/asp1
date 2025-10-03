def water_jug_manual_path():
    steps=[]
    # step1
    a,b=0,0
    steps.append((a,b))
    # step2
    a=5
    steps.append((a,b))
    # step3
    transfer=min(5,4-b)
    a-=transfer
    b+=transfer
    steps.append((a,b))
    # step4
    b=0
    steps.append((a,b))
    # step5
    transfer=min(a,4-b)
    a-=transfer
    b+=transfer
    steps.append((a,b))
    # step6
    a=5
    steps.append((a,b))
    # step7
    transfer=min(a,4-b)
    a-=transfer
    b+=transfer
    steps.append((a,b))
    # step8
    b=0
    steps.append((a,b))
    #print
    print("Steps to reach(2,0): ")
    for idx, state in enumerate(steps):
        print(f"Step {idx}: Jug1={state[0]}L, Jug2={state[1]}L")

water_jug_manual_path()
