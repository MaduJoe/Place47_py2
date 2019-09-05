# Configuration File

# Base directory for data formats
#name = 'GURO_CELL'
#name = 'INBREAST'
name = 'FINAL_TRAIN_NEW_AUG'
# /dataset/places47/image/
#data_base = 'train_image/train_val_4/'
#aug_base = 'train_image/train_val_4/'
#test_dir = 'train_image/train_val_4/'

data_base = '/dataset/places47/image/'
aug_base = '/dataset/places47/image/'
test_dir = '/dataset/places47/image/'

# model option
#batch_size = 16
batch_size = 32
num_epochs = 40
lr_decay_epoch=10
feature_size = 100

# meanstd options
# INBREAST
#mean = [0.60335361908536667, 0.60335361908536667, 0.60335361908536667]
#std = [0.075116530817055119, 0.075116530817055119, 0.075116530817055119]

# GURO_EXTEND
#mean = [0.48359630772217554, 0.48359630772217554, 0.48359630772217554]
#std = [0.13613821516980551, 0.13613821516980551, 0.13613821516980551]

# GURO+INBREAST
mean = [0.51508365254458033, 0.51508365254458033, 0.51508365254458033]
std = [0.12719534902225299, 0.12719534902225299, 0.12719534902225299]
