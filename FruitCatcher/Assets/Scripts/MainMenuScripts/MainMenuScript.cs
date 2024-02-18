using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using TMPro;
using UnityEngine.UI;   

public class MainMenuScript : MonoBehaviour
{
    public GameObject audioSource;

    // Start is called before the first frame update
    void Start()
    {
        GameObject new_audSource = GameObject.Find("AudioManager");
        if(new_audSource == null)
        {
            Destroy(new_audSource);
        }
        else
        {
            if (audioSource)
            {
                DontDestroyOnLoad(audioSource);
            }
        }

        audioSource = GameObject.Find("AudioManager");
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    public  void PlayGame()
    {
        SceneManager.LoadScene("Game");
    }
    public void QuitGame()
    {
        Application.Quit();
    }

    public void SettingsMenu()
    {
        SceneManager.LoadScene("Settings");
    }

    public void BackToMainMenu()
    {
        SceneManager.LoadScene("MainMenu");
    }
}
