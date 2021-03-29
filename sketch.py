from DNA import DNA 
import random 
# Variables needed for GA 
mutationRate = 0.01 
population_size = 500 

population = [] 
matingPool = [] 
# target = "STAY HUNGRY STAY FOOLISH" 
target = "HELLO" 

""" 
Step 1: Initialize. Create a population of N elements, each with randomly generated DNA.
"""
def setup(): 
    for i in range(population_size): 
        population.append(DNA(gene_length=len(target), target=target)) 

def draw(): 
    """
    Step 2: Selection. Evaluate the fitness of each element of the population and build a mating pool.
    """ 

    # Build Mating Pool 
    for i in range(population_size): 
        for j in range(int(population[i].fitness)*100): 
            matingPool.append(population[i]) 
    
    """ 
    Step 3: Reproduction. Repeat N times:
    """ 
    for i in range(population_size): 
        child = random.choice(matingPool).crossover(random.choice(matingPool)) 
        child.mutate(mutationRate=mutationRate) 
        population[i] = child 
    
def evaluate(population, target): 
    for i in population: 
        if "".join(i.genes) == target: 
            return True 
    
    return False 

if __name__ == "__main__": 
    setup() 
    count = 0 

    while(not evaluate(population, target)): 
        draw()     
        print("Generation:", count) 
        
        count+=1 

    for i in population: 
        print("".join(i.genes)) 
        if "".join(i.genes) == target: 
            print("================ Found It ================") 
