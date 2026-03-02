#training Loops
num_epochs = 10
initial_loss = 1.0

for epoch in range (1, num_epochs +1):
    loss = initial_loss / epoch
    accuracy = 1 - (1 / (epoch + 1))

    print(f"Epoch {epoch}/{num_epochs}")
    print(f" Loss: {loss:.4f}")
    print(f" Accuracy : {accuracy:.4f}")
    print("-"*30)


#Batch processing
dataset_size=1000000
batch_size=200

num_batches = dataset_size // batch_size

for batch_num in range(num_batches):
    start_idx = batch_num * batch_size
    end_idx = start_idx + batch_size
    print(f"Processing batch {batch_num+1}: samples{start_idx} to {end_idx}")