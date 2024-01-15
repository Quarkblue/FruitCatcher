using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BasketMovement : MonoBehaviour
{
    private Rigidbody2D rb;
    public float speed,xBound;
    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        
        
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        float h= Input.GetAxisRaw("Horizontal");    

        if(h>0)
        {
            rb.velocity = Vector2.right * speed;
        }
        else if(h<0)
        {
            rb.velocity = Vector2.left * speed;
        }
        else
        {
            rb.velocity = Vector2.zero;
        }   
         transform.position = new Vector2(Mathf.Clamp(transform.position.x, -xBound,xBound), transform.position.y);
        
    }
}
