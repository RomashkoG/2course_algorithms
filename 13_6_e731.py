def to_infix(prefix):
    prec = {'+':1,'-':1,'*':2,'/':2}
    stack = []
    for c in reversed(prefix):
        if c.isalpha():
            stack.append((c, None))
        else:
            left, lop = stack.pop()
            right, rop = stack.pop()
            cp = prec[c]
            def need_paren(child_op, child_prec, is_right):
                if child_op is None:
                    return False
                if child_prec < cp:
                    return True
                if is_right and child_prec == cp and c in '-/':
                    return True
                return False
            lp = prec[lop] if lop else 0
            rp = prec[rop] if rop else 0
            if need_paren(lop, lp, False):
                left = f'({left})'
            if need_paren(rop, rp, True):
                right = f'({right})'
            expr = left + c + right
            stack.append((expr, c))
    return stack[0][0]

s = input().strip()
print(to_infix(s))