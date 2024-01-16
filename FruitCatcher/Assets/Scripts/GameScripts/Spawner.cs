using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawner : MonoBehaviour
{
    public GameObject[] fruits;
    public GameObject bomb;

    public float xBounds;
    public float yBound;
    public float objectSpeed; // Add this variable for speed

    // Start is called before the first frame update
    void Start()
    {
        StartCoroutine("SpawnRandomGameObject");
    }

    IEnumerator SpawnRandomGameObject()
    {
        yield return new WaitForSeconds(Random.Range(1, 2));

        int randomFruit = Random.Range(0, fruits.Length);

        GameObject spawnedObject;

        if (Random.value <= 0.6f)
            spawnedObject = Instantiate(fruits[randomFruit], new Vector2(Random.Range(-xBounds, xBounds), yBound), Quaternion.identity);
        else
            spawnedObject = Instantiate(bomb, new Vector2(Random.Range(-xBounds, xBounds), yBound), Quaternion.identity);

        // Set the speed of the spawned object
        spawnedObject.GetComponent<Rigidbody2D>().velocity = new Vector2(0, -objectSpeed);

        StartCoroutine("SpawnRandomGameObject");
    }

}
