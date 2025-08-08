# organize_dataset.py
import pandas as pd
import os
import shutil
from tqdm import tqdm
import logging
import tensorflow as tf

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(_name_)

# Dataset structure paths
DATASET_STRUCTURE = {
    'raw': 'dataset/raw',
    'processed': 'dataset/processed',
    'train': 'dataset/train',
    'val': 'dataset/val', 
    'test': 'dataset/test',
    'models': 'dataset/models',
    'results': 'dataset/results'
}

# Diabetic Retinopathy classes
CLASSES = {
    '0': 'No DR',
    '1': 'Mild DR', 
    '2': 'Moderate DR',
    '3': 'Severe DR',
    '4': 'Proliferative DR'
}

def create_dataset_structure():
    """Create the complete dataset directory structure"""
    logger.info("Creating dataset directory structure...")
    
    for path in DATASET_STRUCTURE.values():
        os.makedirs(path, exist_ok=True)
        logger.info(f"Created directory: {path}")
    
    # Create class directories for train, val, test
    for split in ['train', 'val', 'test']:
        for class_id in CLASSES.keys():
            class_dir = os.path.join(DATASET_STRUCTURE[split], class_id)
            os.makedirs(class_dir, exist_ok=True)
            logger.info(f"Created class directory: {class_dir}")

def organize_images(csv_path, source_img_dir, target_dir, split_name):
    """
    Organize images from CSV file into class-based directories
    
    Args:
        csv_path: Path to CSV file with image IDs and labels
        source_img_dir: Directory containing source images
        target_dir: Target directory for organized images
        split_name: Name of the split (train/val/test)
    """
    if not os.path.exists(csv_path):
        logger.error(f"CSV file not found: {csv_path}")
        return
    
    if not os.path.exists(source_img_dir):
        logger.error(f"Source image directory not found: {source_img_dir}")
        return
    
    df = pd.read_csv(csv_path)
    logger.info(f"Processing {len(df)} images for {split_name} split")
    
    successful_copies = 0
    missing_files = 0
    
    for _, row in tqdm(df.iterrows(), total=len(df), desc=f"Organizing {split_name}"):
        filename = row['id_code'] + ".png"
        label = str(row['diagnosis'])
        
        src_path = os.path.join(source_img_dir, filename)
        label_dir = os.path.join(target_dir, label)
        dst_path = os.path.join(label_dir, filename)
        
        if os.path.exists(src_path):
            try:
                shutil.copy2(src_path, dst_path)
                successful_copies += 1
            except Exception as e:
                logger.error(f"Error copying {src_path}: {e}")
        else:
            missing_files += 1
            logger.warning(f"File not found: {src_path}")
    
    logger.info(f"{split_name} split complete: {successful_copies} copied, {missing_files} missing")

def organize_dataset():
    """Main function to organize the entire dataset"""
    logger.info("Starting dataset organization...")
    
    # Create directory structure
    create_dataset_structure()
    
    # Define source paths (update these based on your actual dataset location)
    source_paths = {
        'train': {
            'csv': r"C:\Users\LENOVO\OneDrive\Desktop\archive (1)\train_1.csv",
            'images': r"C:\Users\LENOVO\OneDrive\Desktop\archive (1)\train_images\train_images"
        },
        'val': {
            'csv': r"C:\Users\LENOVO\OneDrive\Desktop\archive (1)\valid.csv",
            'images': r"C:\Users\LENOVO\OneDrive\Desktop\archive (1)\val_images\val_images"
        },
        'test': {
            'csv': r"C:\Users\LENOVO\OneDrive\Desktop\archive (1)\test.csv",
            'images': r"C:\Users\LENOVO\OneDrive\Desktop\archive (1)\test_images\test_images"
        }
    }
    
    # Organize each split
    for split_name, paths in source_paths.items():
        if split_name in DATASET_STRUCTURE:
            target_dir = DATASET_STRUCTURE[split_name]
            organize_images(
                csv_path=paths['csv'],
                source_img_dir=paths['images'], 
                target_dir=target_dir,
                split_name=split_name
            )
    
    logger.info("Dataset organization complete!")
    print_dataset_stats()

def print_dataset_stats():
    """Print statistics about the organized dataset"""
    logger.info("Dataset Statistics:")
    logger.info("=" * 50)
    
    for split in ['train', 'val', 'test']:
        split_dir = DATASET_STRUCTURE[split]
        total_images = 0
        
        logger.info(f"\n{split.upper()} Split:")
        for class_id, class_name in CLASSES.items():
            class_dir = os.path.join(split_dir, class_id)
            if os.path.exists(class_dir):
                num_images = len([f for f in os.listdir(class_dir) if f.endswith('.png')])
                total_images += num_images
                logger.info(f"  Class {class_id} ({class_name}): {num_images} images")
        
        logger.info(f"  Total {split} images: {total_images}")

if _name_ == "_main_":
    organize_dataset()
