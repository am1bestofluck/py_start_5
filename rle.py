

def main(inc:str) -> str:    
    out = ""
    tmp = 1
    for i in range(len(inc)):
        try:
            if inc[i+1] == inc[i]:
                tmp += 1
            else:
                out += f"{tmp}{inc[i]}"
                tmp = 1
        except IndexError:
            if inc[-1] == inc [-2]:
                out += f"{tmp}{inc[i]}"
            else:
                out += f"{tmp}{inc[i]}"

    return out
    
print(main("111112222334445"))
assert main("111112222334445") == "5142233415"
print(main("AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE")) 
assert main("AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE") == "6A1F2D7C1A17E"
print(main("AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEEq")) 
assert main("AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEEq") == "6A1F2D7C1A17E1q"   