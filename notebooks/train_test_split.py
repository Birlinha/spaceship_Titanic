from sklearn.model_selection import train_test_split

def tt_split(X,Y):
    X1,X2,y1,y2 = train_test_split(
                            X, Y,
                            test_size=0.2,
                            random_state=97,
                            shuffle=True, stratify=None)
    
    return X1, X2, y1, y2