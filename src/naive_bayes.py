import numpy as np

#naive bayes model
def p(j,X,y): 
    total=0
    for i in y:
        # print(i)
        # print(f"j={j}")
        if j==i:
            total+=1
    return total/(X.shape[0]-1)

def normal(x, mu, var):
    return np.sqrt(1/(2*np.pi*var))*(np.exp(-(1/(2*var))*(x-mu)**2))

def N(x,i,j,X,y):
    X_kj=X[np.where(y==i),j]
    X_kj=set(np.ravel(np.array(X_kj)))
    mu=sum(X_kj)/sum([1 for item in y if item==i])
    Ex=sum([a*p(a,X,X_kj) for a in X_kj])
    Ex2=sum([a**2*p(a,X,X_kj) for a in X_kj])
    var=np.abs(Ex2-Ex**2)
    if var==0:
        var=0.1
    return normal(x[j],mu, var)
    
def bayes_prediction(x,X,y):
    label=0
    label_p=0
    for i in range(-2,3):
        theta=sum([1 for item in y if item==i])/X.shape[0]
        l=theta
        for j in range(X.shape[1]):
            l*=N(x,i,j,X,y)
        if l>label_p:
            label_p=l
            label=i
    return label