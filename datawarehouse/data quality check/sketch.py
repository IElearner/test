import mytests
tests = {key: value for key, value in mytests.__dict__.items() if key.startswith('test')}
print(tests.items())
for testname, test in tests.items():
    print(test)

print('2')