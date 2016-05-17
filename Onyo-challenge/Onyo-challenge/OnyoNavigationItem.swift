//
//  OnyoNavigationItem.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/15/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import UIKit

extension UINavigationItem {

    func config() {
        titleView = UIImageView(image:UIImage(named: "logo_navigation_bar"))
        rightBarButtonItem = UIBarButtonItem(image: UIImage(named: "onyo"), style: .Done, target: self, action: nil)
    }
    
}
