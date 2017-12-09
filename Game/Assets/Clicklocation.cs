using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Clicklocation : MonoBehaviour {

    public double range = 10;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        if (Input.GetMouseButtonDown(0))
        {
            Vector3 mouseVec = Input.mousePosition;
            string mousePos = mouseVec.ToString();
            

            for(int i = 0; i < 900; i++)
            {
                if (Uploadtextscript.x[i] != 0 && Uploadtextscript.y[i] != 0)
                {
                    if ((Uploadtextscript.x[i] - range) < mouseVec.x && mouseVec.x < (Uploadtextscript.x[i] + range))
                    {
                        if ((Uploadtextscript.y[i] - range) < mouseVec.y && mouseVec.y < (Uploadtextscript.y[i] + range))
                        {
                            GlobalControl.coins++;
                            GameObject.Find("Text").GetComponent<Text>().text = "Total Score = " + GlobalControl.coins;
                            Uploadtextscript.x[i] = 0;
                            Uploadtextscript.y[i] = 0;
                            Debug.Log("SCORE");
                        }
                    }
                }
                //Debug.Log("looped");
            }
            Debug.Log("CLICKED: " + mousePos);

        }
    }

    private void OnMouseDown()
    {
        
    }
}
