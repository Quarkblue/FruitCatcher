using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BasketMovement : MonoBehaviour
{
    private Rigidbody2D rb;
    public float speed,xBound;
    // Start is called before the first frame update

    public BasketMovement Instance;
    public bool StartRecieving = false;

    public string movement;

    private void Awake()
    {
        if (PlayerPrefs.HasKey("Speed"))
        {
            speed = PlayerPrefs.GetInt("Speed");
        }
        else
        {
            speed = 25;
        }
    }

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        StartRecieving = true;
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        float h= Input.GetAxisRaw("Horizontal");    

        if(h>0 || movement == "right hand up")
        {
            rb.velocity = Vector2.right * speed;
        }
        else if(h<0 || movement == "left hand up")
        {
            rb.velocity = Vector2.left * speed;
        }
        else if(h == 0 || movement == "both hands down")
        {
            rb.velocity = Vector2.zero;
        }   
         transform.position = new Vector2(Mathf.Clamp(transform.position.x, -xBound,xBound), transform.position.y);
        
    }
}
