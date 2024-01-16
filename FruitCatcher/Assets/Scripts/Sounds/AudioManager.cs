using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AudioManager : MonoBehaviour
{
    [SerializeField] AudioSource music; 
    public AudioClip background;
    // Start is called before the first frame update

    public static AudioManager instance;    

    private void Awake()
    {
        if(instance == null)
            instance = this;
        else
            Destroy(this.gameObject);   
        DontDestroyOnLoad(this.gameObject);
    }
    
    void Start()
    {
        music.clip = background;    
        music.Play();   
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
