import asyncio
import time
from asyncio import sleep


async def study_physics():
    print('Studying physics...')
    print('Let\' wait..')
    await sleep(.3)  # waiting
    print('Completing physics work')
    return 'physics done'


async def study_maths():
    print('Studying maths...')
    print('Let\' wait for paper..')
    await sleep(.3)  # waiting
    print('Completing maths work')
    return 'maths done'


async def main():
    start_time = time.time()
    batch = asyncio.gather(study_physics(), study_maths())
    [physics, maths] = await batch
    print(physics, '|', maths)
    end_time = time.time()

    print(f'Delta: {end_time - start_time}')


if __name__ == '__main__':
    asyncio.run(main())
