# Train a policy

## Quickstart

First, install learning-related dependencies:
```bash
poetry install --with learning
```

Now we can start training:
```python
python ppo.py --env-id A1-v4
```

## Logging to Weights and Biases. 

We support WandB logging as follows. 

```python
python ppo.py \
    --env-id A1-v4 \
    --wandb-entity <YOUR-ENTITY> \
    --wandb-project <YOUR-PROJECT> \
    --track
```