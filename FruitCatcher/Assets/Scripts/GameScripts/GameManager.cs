using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameManager : MonoBehaviour
{
    public int timer;
    public GameObject StartTimer;

    public bool isPaused;

    public static GameManager Instance;
    private void OnEnable()
    {
        EventManager.onGameOver += GameOver;
    }

    private void Awake()
    {
        Instance = this;
    }
    void Start()
    {
        Time.timeScale = 0;
        StartCoroutine(WaitOnes());
    }
    void Update()
    {
        if(timer <= 0)
        {
            if (!isPaused)
            {
                Time.timeScale = 1;
            }
        }
    }

    private void OnDisable()
    {
        EventManager.onGameOver -= GameOver;
    }
        
    private IEnumerator WaitOnes()
    {
        while (timer > 0 && true)
        {
            StartTimer.GetComponent<TMPro.TextMeshProUGUI>().text = timer.ToString();
            yield return new WaitForSecondsRealtime(1f);
            timer--;
        }
    }

    public void GameOver()
    {

    }

}
