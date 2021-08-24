animals={"turtle","horse","robin","python","swallow","hedgehog","wren","aardvark","cat"}
birds={"robin","swallow","wren"}

print(f"bird is subset of animals : {birds.issubset(animals)}")
print(f"animal is superset of birds : {animals.issuperset(birds)}")

print(birds<=animals)   # bird is subset of animla
print(birds<animals)  #bird is proper subset of animal
