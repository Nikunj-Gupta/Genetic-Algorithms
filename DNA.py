import string 
import random 


class DNA: 
    def __init__(self, gene_length, target): 
        self.gene_length = gene_length 
        self.target=target 
        self.genes = random.choices(string.ascii_uppercase + string.digits, k = gene_length) 
        self.fitness = self.calcFitness() 
    
    def calcFitness(self): 
        return len(set("".join(self.genes)) & set(self.target)) 

    def crossover(self, partner): 
        mid = random.randint(0, self.gene_length) 
        child = DNA(gene_length=self.gene_length, target=self.target) 
        child.genes = self.genes[0:mid] + partner.genes[mid:self.gene_length] 

        return child 

    def mutate(self, mutationRate): 
        for i in range(self.gene_length): 
            if (random.random() < mutationRate): 
                self.genes[i] = random.choice(string.ascii_letters) 

