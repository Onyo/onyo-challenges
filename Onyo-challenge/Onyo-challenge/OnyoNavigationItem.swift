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
        titleView = UIImageView(image:UIImage(named: "icon-bakedPotato"))
        rightBarButtonItem = UIBarButtonItem(image: UIImage(named: "icon-onyo"), style: .Done, target: self, action: nil)
    }
    
}
