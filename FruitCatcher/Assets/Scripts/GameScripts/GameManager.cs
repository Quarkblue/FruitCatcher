using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    public int timer;
    public GameObject StartTimer;
    public float timeTaken;
    public TMPro.TextMeshProUGUI timerText;

    public GameObject Basket;

    public ScoreManager scoreManager;

    public bool isPaused;

    string niceTime;

    public static GameManager Instance;
    private void OnEnable()
    {
        EventManager.onGameOver += GameOver;
    }

    private void Awake()
    {
        Instance = this;
        niceTime = "0:00";
    }
    void Start()
    {
        scoreManager = Basket.GetComponent<ScoreManager>();
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
                StartTimer.SetActive(false);

                timeTaken += Time.deltaTime;

                int minutes = Mathf.FloorToInt(timeTaken / 60F);
                int seconds = Mathf.FloorToInt(timeTaken - minutes * 60);

                niceTime = string.Format("{0:0}:{1:00}", minutes, seconds);

                timerText.text = $"Timer: {niceTime}";
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
        PlayerPrefs.SetString("TimeTaken", niceTime);
        PlayerPrefs.SetInt("Score", scoreManager.score);
        SceneManager.LoadScene("GameOver");
    }
}