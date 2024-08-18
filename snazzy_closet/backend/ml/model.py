from tensorflow.keras.applications import MobileNet # type: ignore
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D # type: ignore
from tensorflow.keras.models import Model # type: ignore

def build_model(num_classes):
    # Load pre-trained MobileNet model
    base_model = MobileNet(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
        
    # Add custom layers on top of the base model
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    
    # Save the trained model to a file. 
    # Consider implementing a versioning strategy (e.g., timestamp-based or semantic versioning)
    # to avoid overwriting models if this script is run multiple times. 
    # This is especially important in a CI/CD pipeline or production environment to maintain 
    # a history of trained models for rollback or analysis.
    model = Model(inputs=base_model.input, outputs=predictions)
    
    return model
